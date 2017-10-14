
import codecs
import datetime
import json

from app import key
from app.communicator import sender

class Transaction():

    message = ''
    time_stamp = datetime.datetime.now()

    def to_json(self):
        return "Transaction"
        '''
        return json.dumps({
            'time_stamp': self.time_stamp,
            'message': self.message
        })'''


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
