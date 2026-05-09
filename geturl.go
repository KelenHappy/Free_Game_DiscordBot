package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	firebase "firebase.google.com/go/v4"
	"firebase.google.com/go/v4/db"
	"google.golang.org/api/option"
)

// Need setup Firebase

var firebaseDB *db.Client

func initFirebase() error {
	if firebaseDB != nil {
		return nil
	}

	opt := option.WithCredentialsFile("serviceAccountKey.json")
	config := &firebase.Config{
		DatabaseURL: "your firebase url", // Change to your Firebase URL
	}

	app, err := firebase.NewApp(context.Background(), config, opt)
	if err != nil {
		return fmt.Errorf("firebase init error: %w", err)
	}

	firebaseDB, err = app.Database(context.Background())
	if err != nil {
		return fmt.Errorf("firebase database error: %w", err)
	}

	return nil
}

type APIResponse struct {
	Data struct {
		Results []struct {
			CanonicalURL string `json:"canonicalUrl"`
		} `json:"results"`
	} `json:"data"`
}

type FirebaseData struct {
	Data string `json:"data"`
}

// GetURL fetches the API, compares with the last stored URL in Firebase,
// and returns any new URLs (in chronological order, oldest first).
func GetURL(apiURL string) ([]string, error) {
	if err := initFirebase(); err != nil {
		return nil, fmt.Errorf("FIREBASE INIT ERROR: %w", err)
	}

	ctx := context.Background()

	// 1. Read last known URL from Firebase
	ref := firebaseDB.NewRef("/")
	var stored FirebaseData
	if err := ref.Get(ctx, &stored); err != nil {
		return nil, fmt.Errorf("FIREBASE READ ERROR: %w", err)
	}
	lastURL := stored.Data

	// 2. Fetch the API
	resp, err := http.Get(apiURL) //nolint:gosec
	if err != nil {
		return nil, fmt.Errorf("REQUEST ERROR: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		return nil, fmt.Errorf("REQUEST ERROR: status %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("READ ERROR: %w", err)
	}

	var apiResp APIResponse
	if err := json.Unmarshal(body, &apiResp); err != nil {
		return nil, fmt.Errorf("JSON ERROR: %w", err)
	}

	// 3. Extract canonical URLs
	var newURLs []string
	for _, item := range apiResp.Data.Results {
		if item.CanonicalURL != "" {
			newURLs = append(newURLs, item.CanonicalURL)
		}
	}

	if len(newURLs) == 0 {
		fmt.Println("No new URLs found.")
		return []string{}, nil
	}

	// 4. Collect URLs that are newer than lastURL
	var answerBack []string
	if lastURL != "" {
		for _, u := range newURLs {
			if u == lastURL {
				break
			}
			answerBack = append(answerBack, u)
		}
	}
	else {
		// No stored URL yet — return only the first (latest) entry
		answerBack = []string{newURLs[0]}
	}

	// 5. Reverse to chronological order (oldest first)
	for i, j := 0, len(answerBack)-1; i < j; i, j = i+1, j-1 {
		answerBack[i], answerBack[j] = answerBack[j], answerBack[i]
	}

	// 6. Update Firebase with the newest URL
	if len(answerBack) > 0 {
		if err := ref.Update(ctx, map[string]interface{}{"data": newURLs[0]}); err != nil {
			return nil, fmt.Errorf("FIREBASE WRITE ERROR: %w", err)
		}
	}

	return answerBack, nil
}
