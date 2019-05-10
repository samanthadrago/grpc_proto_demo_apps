import grpc

import transaction_pb2_grpc


channel = grpc.insecure_channel('localhost:50051',
    options=[('grpc.max_receive_message_length', 
        6 * 1024 * 1024)])

stub = transaction_pb2_grpc.TransactionServiceStub(channel)
