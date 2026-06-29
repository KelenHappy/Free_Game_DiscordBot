package main

import (
	"fmt"
	"log"
	"os"
	"time"
	"github.com/bwmarrin/discordgo"
	"github.com/joho/godotenv"
)

const (
	apiURL = "https://www.4gamers.com.tw/site/api/news/of-category/1118?nextStart=0&pageSize=25"
)

func runJob(s *discordgo.Session, channelID string) {
	fmt.Println("Executing the code")

	urls, err := GetURL(apiURL)
	if err != nil {
		log.Printf("GetURL error: %v", err)
		return
	}

	if len(urls) == 0 {
		fmt.Println("No new URLs were detected.")
		return
	}

	for _, u := range urls {
		message := fmt.Sprintf("New URL found: %s", u)
		if _, err := s.ChannelMessageSend(channelID, message); err != nil {
			log.Printf("Failed to send message: %v", err)
		} else {
			fmt.Println(u)
		}
		time.Sleep(200 * time.Millisecond)
	}

	fmt.Println("Job completed.")
}

func main() {
	_ = godotenv.Load() // Read .env, skip if not found

	token := os.Getenv("BOT_TOKEN")
	if token == "" {
		log.Fatal("BOT_TOKEN environment variable not set.")
	}

	// Create Discord session
	dg, err := discordgo.New("Bot " + token)
	if err != nil {
		log.Fatalf("Error creating Discord session: %v", err)
	}
	dg.Identify.Intents = discordgo.IntentsGuildMessages

	channelID := os.Getenv("CHANNEL_ID")
	if channelID == "" {
		log.Fatal("CHANNEL_ID environment variable not set.")
	}

	done := make(chan struct{})

	// On ready: execute job then close
	dg.AddHandler(func(s *discordgo.Session, r *discordgo.Ready) {
		fmt.Printf("「%s」has logged in\n", s.State.User.Username)
		runJob(s, channelID)
		dg.Close()
		close(done)
	})

	// Open connection
	if err := dg.Open(); err != nil {
		log.Fatalf("Error opening Discord connection: %v", err)
	}

	<-done
}
