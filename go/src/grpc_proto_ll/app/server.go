package main

import (
    "encoding/json"
    // "fmt"
    "log"
    "grpc_proto_ll/db"
    "net/http"
    "github.com/golang/protobuf/proto"
    "github.com/gorilla/mux"
)


func returnJson(w http.ResponseWriter) {
    // Parse transactions into Go structs from CSV database
    transactions := db.ReadFromCsv()

    // Marshal into JSON to return
    returnData, _ := json.Marshal(transactions)
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    w.Write(returnData)
}

func returnProto(w http.ResponseWriter) {
    // Parse transactions into Go structs from CSV database
    transactions := db.ReadFromCsv()

    // Marshal into Proto to return

    returnData, _ := proto.Marshal(transactions)
    w.Write(returnData)
}

func handler(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    dataFormat := vars["format"]
    if dataFormat == "json" {
        returnJson(w)
    } else {
        returnProto(w)
    }
}

func main() {

    router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/transactions/{format}", handler)
    log.Fatal(http.ListenAndServe(":8081", router))
}
