import datetime
import enum
import time
import sys
from typing import List
import requests

from bottle import route, run, template

from grpc_client import stub
import transaction_pb2

class AccountType(enum.Enum):
    BANK = 'bank'
    CREDIT_CARD = 'credit_card'


class Transaction:
    def __init__(self, 
                 account_id: int,
                 # account_type: str,
                 amount: float,
                 transaction_date: int,
                 description: str,
                 fx_rate: float):
        self.account_id = account_id
        # self.account_type = AccountType.BANK if account_type == 'BANK' else AccountType.CREDIT_CARD
        self.amount = amount
        self.transaction_date = datetime.datetime.utcfromtimestamp(
            transaction_date)
        self.description = description
        self.fx_rate = fx_rate

    @classmethod
    def from_json(cls, json):
        return cls(
            account_id=json['account_id'],
            # account_type=json['account_type'],
            amount=json['amount'],
            transaction_date=json['transaction_date'],
            description=json['description'],
            fx_rate=json['fx_rate'])


class Transactions:
    def __init__(self,
                 transactions_list: List[Transaction]):
        self.transactions = transactions_list

    @classmethod
    def from_json(cls, json):
        return cls(
                transactions_list=[
                    Transaction.from_json(trans_json) for trans_json in json['transactions']]
            )


def _parse_json_to_python(json_data):
    return Transactions.from_json(json_data)


def _parse_proto_to_python(proto_data):
    transactions = transaction_pb2.Transactions()
    transactions.ParseFromString(proto_data)
    return transactions

def fetch_json_transactions():
    """Fetch transactions from Go service, deserialize
    into Python objects, and return number of transactions
    """
    res = requests.get(
        'http://localhost:8081/transactions/json')
    byte_size = sys.getsizeof(res.content)
    print(f'json size: {byte_size}')
    python_transactions = _parse_json_to_python(res.json())
    return len(python_transactions.transactions)


def fetch_proto_transactions():
    """Fetch transactions from Go service, deserialize
    into Python objects, and return number of transactions
    """
    raw_data = requests.get(
        'http://localhost:8081/transactions/proto').content
    byte_size = sys.getsizeof(raw_data)
    print(f'proto size: {byte_size}')
    python_transactions = _parse_proto_to_python(raw_data)
    return len(python_transactions.transactions)


@route('/transactions/<format>')
def get_transactions(format):
    t0 = time.time()

    # Fetch transactions of the requested format
    if format == 'json':
        data = fetch_json_transactions()
        filename = 'timings_json.txt'
    elif format == 'proto':
        data = fetch_proto_transactions()
        filename = 'timings_proto.txt'
    else:
        raise Exception(f'No format called {format}')

    total_time = (time.time() - t0) * 1000
    return template('Fetched {{data}} transactions in format {{format}}. '
                    'Took {{length}}ms.', 
        data=data, format=format, length=total_time)


@route('/grpc')
def grpc():
    t0 = time.time()
    request = transaction_pb2.FetchRequest()
    data = stub.FetchTransactions(request)
    total_time = (time.time() - t0) * 1000
    return template('Fetched {{data}} transactions via gRPC. '
                    'Took {{length}}ms.', 
        data=len(data.transactions), length=total_time)

run(host='localhost', port=8080, debug=True)
