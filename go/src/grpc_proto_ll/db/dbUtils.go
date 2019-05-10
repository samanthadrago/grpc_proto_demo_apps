/*
 * Utils for interacting with the DB
 */
package db 

import (
    "bufio"
    "encoding/csv"
    // "fmt"
    "io"
    "os"
    "grpc_proto_ll/pb"
    "strconv" 
)


func ReadFromCsv() (*pb.Transactions){
    csvFile, _ := os.Open("../data/transactions.csv")
    defer csvFile.Close()
    reader := csv.NewReader(bufio.NewReader(csvFile))
    transactions := &pb.Transactions{}
    
    for {
        line, error := reader.Read()
        if error == io.EOF {
            break
        } 

        accountType := pb.Transaction_BANK

        if line[1] == "credit_card" {
            accountType = pb.Transaction_CREDIT_CARD
        }

        accountId, _ := strconv.ParseInt(line[0], 10, 32)
        accountId32 := int32(accountId)
        amount, _ := strconv.ParseFloat(line[2], 32)
        amount32 := float32(amount)
        fxRate, _ := strconv.ParseFloat(line[4], 32)
        fxRate32 := float32(fxRate)
        transactionDate, _ := strconv.ParseInt(line[5], 10, 32)
        transactionDate32 := int32(transactionDate)

        newTransaction := pb.Transaction{
            AccountId: accountId32,
            AccountType:  accountType,
            Amount: amount32,
            Description: line[3],
            FxRate: fxRate32,
            TransactionDate: transactionDate32,
        }
        transactions.Transactions = append(transactions.Transactions, &newTransaction)
    }

    return transactions
}
