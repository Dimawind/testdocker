package main

import (
    "context"
    "database/sql"
    "encoding/json"
    "fmt"
    "log"
    "math/rand"
    "net/http"
    "sync"
    "time"
	"os"

    "github.com/jackc/pgx/v4"
    "github.com/pressly/goose/v3"
    _ "github.com/lib/pq"
)

func main() {
    var err error
    dbURL := os.Getenv("DATABASE_URL")
    db, err = pgx.Connect(context.Background(), dbURL)
    // остальной код
}

var (
    db     *pgx.Conn
    mu     sync.Mutex
    users  = []string{}
)

func main() {
    var err error
    db, err = pgx.Connect(context.Background(), "postgres://username:password@localhost:5432/yourdb")
    if err != nil {
        log.Fatalf("Unable to connect to database: %v\n", err)
    }
    defer db.Close(context.Background())

    // Выполнение миграций
    if err := goose.Up(db, "migrations"); err != nil {
        log.Fatalf("Failed to run migrations: %v\n", err)
    }

    http.HandleFunc("/get-users", getUsersHandler)
    go createUserEvery5Seconds()
    go fetchUsersEverySecond()

    log.Println("Server is running on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func getUsersHandler(w http.ResponseWriter, r *http.Request) {
    mu.Lock()
    defer mu.Unlock()

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(users)
}

func createUserEvery5Seconds() {
    for {
        time.Sleep(5 * time.Second)
        mu.Lock()
        userName := fmt.Sprintf("User%d", rand.Intn(1000))
        users = append(users, userName)
        mu.Unlock()
        log.Printf("Created user: %s\n", userName)
    }
}

func fetchUsersEverySecond() {
    for {
        time.Sleep(1 * time.Second)
        mu.Lock()
        log.Println("Fetching users...")
        mu.Unlock()
        // Здесь можно добавить логику для запроса пользователей с сервера
        // Например, с помощью http.Get
    }
}
