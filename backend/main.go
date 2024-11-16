package main

import (
	"backend/handlers"
	"log"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	// Serve the frontend
	router.Static("/static", "../src")

	// API endpoint for punching in
	router.POST("/api/punchin", handlers.PunchIn)

	// Start the server on port 8080
	if err := router.Run(":8080"); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
