package main

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"strconv"
	"syscall"
	"time"

	"github.com/bwmarrin/discordgo"
	"github.com/joho/godotenv"
)

const (
	apiURL              = "https://www.4gamers.com.tw/site/api/news/of-category/1118?nextStart=0&pageSize=25"
	defaultCheckMinutes = 30
)

func checkInterval(value string) (time.Duration, error) {
	if value == "" {
		return defaultCheckMinutes * time.Minute, nil
	}

	minutes, err := strconv.Atoi(value)
	if err != nil || minutes <= 0 || minutes > int(time.Duration(1<<63-1)/time.Minute) {
		return 0, fmt.Errorf("CHECK_INTERVAL_MINUTES must be a positive integer, got %q", value)
	}

	return time.Duration(minutes) * time.Minute, nil
}

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

	interval, err := checkInterval(os.Getenv("CHECK_INTERVAL_MINUTES"))
	if err != nil {
		log.Fatal(err)
	}

	ready := make(chan struct{}, 1)
	dg.AddHandler(func(s *discordgo.Session, r *discordgo.Ready) {
		fmt.Printf("「%s」has logged in\n", s.State.User.Username)
		select {
		case ready <- struct{}{}:
		default:
		}
	})

	// Open connection
	if err := dg.Open(); err != nil {
		log.Fatalf("Error opening Discord connection: %v", err)
	}
	defer dg.Close()

	<-ready
	log.Printf("Checking for free games every %s.", interval)
	runJob(dg, channelID)

	ticker := time.NewTicker(interval)
	defer ticker.Stop()

	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)
	defer signal.Stop(stop)

	for {
		select {
		case <-ticker.C:
			runJob(dg, channelID)
		case <-stop:
			log.Println("Shutting down.")
			return
		}
	}
}
