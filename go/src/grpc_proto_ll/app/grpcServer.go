package main

import (
    "context"
    "grpc_proto_ll/db"
    "grpc_proto_ll/pb"
    "log"
    "net"
    "google.golang.org/grpc"
)


type server struct{}

func (s *server) FetchTransactions(ctx context.Context, in *pb.FetchRequest) (*pb.Transactions, error) {
    log.Printf("Received request")
    transactions := db.ReadFromCsv()
    return transactions, nil
}

func main() {
    lis, err := net.Listen("tcp", "localhost:50051")
    if err != nil {
        log.Fatalf("failed to listen: %v", err)
    }
    s := grpc.NewServer()
    pb.RegisterTransactionServiceServer(s, &server{})
    if err := s.Serve(lis); err != nil {
        log.Fatalf("failed to serve: %v", err)
    }
}
