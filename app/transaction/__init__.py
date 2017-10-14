
import codecs
import datetime
import json

from dateutil import parser
from app import key
from app.communicator import sender

transaction_list = []


class Transaction():

    type = ''
    time_stamp = ''
    tx_id = ''
    pub_key = ''
    message = ''
    signature = ''

    def __init__(self):
        self.type = 'T'
        self.time_stamp = datetime.datetime.now()
        self.tx_id = self.type + self.time_stamp.strftime('%Y%m%d%H%M%S')
        self.pub_key = ''
        self.message = ''
        self.signature = ''

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps({
            'type': self.type,
            'time_stamp': self.time_stamp.strftime('%Y%m%d%H%M%S'),
            'tx_id': self.tx_id,
            'pub_key': self.pub_key,
            'message': self.message,
            'signature': self.signature
        })

    def from_json(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

        self.time_stamp = parser.parse(self.time_stamp)
        return self


def add_transaction(tx):
    transaction_list.append(tx)


def get_transactions():
    return transaction_list


def count():
    return transaction_list.count()


def remove_all():
    transaction_list.clear()


def create_tx(pub_key, pri_key, msg):
    tx = Transaction()
    tx.message = msg

    msg = tx.time_stamp.strftime('%Y%m%d%H%M%S') + msg

    pub_key_b = key.key_to_string(pub_key)

    # transaction 에 공개키 저장
    tx.pub_key = codecs.encode(pub_key_b, 'hex_codec').decode('utf-8')

    sig = key.get_signature(msg, pri_key)

    # transaction에 암호화된 메시지 저장
    tx.signature = codecs.encode(sig, 'hex_codec').decode('utf-8')

    return tx


def send_tx(tx):
    # 모든 노드에 transaction 전송
    sender.send_to_all_node(tx.to_json())


if __name__ == '__main__':
    # 트랜잭션 생성
    # 트랜잭션 전송
    a = ''
