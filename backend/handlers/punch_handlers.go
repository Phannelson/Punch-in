package handlers

import (
	"backend/database"
	"backend/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func PunchIn(c *gin.Context) {
	var punch models.Punch

	if err := c.ShouldBindJSON(&punch); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid data"})
		return
	}

	if err := database.SavePunch(punch); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Unable to save punch-in"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"status": "Punch-in successful"})
}
