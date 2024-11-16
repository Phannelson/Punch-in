package models

import "time"

type Punch struct {
	ID        int       `json:"id"`
	Employee  string    `json:"employee"`
	Timestamp time.Time `json:"timestamp"`
	Pin       string    `json:"pin"`
}
