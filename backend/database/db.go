package database

import (
	"backend/models"
	"database/sql"
	"log"

	_ "github.com/lib/pq"
)

var db *sql.DB

func InitDB() {
	var err error
	connStr := "user=username dbname=punchindb sslmode=disable password=yourpassword"
	db, err = sql.Open("postgres", connStr)
	if err != nil {
		log.Fatalf("Unable to connect to the database: %v", err)
	}

	if err = db.Ping(); err != nil {
		log.Fatalf("Unable to reach the database: %v", err)
	}
}

func SavePunch(punch models.Punch) error {
	query := `INSERT INTO punches (employee, timestamp, pin) VALUES ($1, $2, $3)`
	_, err := db.Exec(query, punch.Employee, punch.Timestamp, punch.Pin)
	return err
}
