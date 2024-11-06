package main

import(
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/PunchInHandle", PunchInHandleFunc)
	http.HandleFunc("/MilesLogsHandle", MilesLogHandleFunc)

	http.ListenAndServe("localhost:8080", nil)
}

func PunchInHandleFunc(w http.ResponseWriterm r *http.Request){
	fmt.Fprint(w, "Hello, World!")
}