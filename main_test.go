package main

import (
	"testing"
	"time"
)

func TestCheckInterval(t *testing.T) {
	tests := []struct {
		name    string
		value   string
		want    time.Duration
		wantErr bool
	}{
		{name: "default", want: 30 * time.Minute},
		{name: "configured", value: "60", want: time.Hour},
		{name: "zero", value: "0", wantErr: true},
		{name: "negative", value: "-5", wantErr: true},
		{name: "not a number", value: "hourly", wantErr: true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := checkInterval(tt.value)
			if (err != nil) != tt.wantErr {
				t.Fatalf("checkInterval(%q) error = %v, wantErr %v", tt.value, err, tt.wantErr)
			}
			if got != tt.want {
				t.Errorf("checkInterval(%q) = %v, want %v", tt.value, got, tt.want)
			}
		})
	}
}
