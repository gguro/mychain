import os
import datetime


from app import *
from app import util, key, node, transaction

from app.communicator import receiver, sender
from app.node import Node
from app.block import Block
from app.consensus.merkle_tree import merkle_tree
from app.consensus.pow import proof_of_work

listen_thread = None
BASE_PATH = os.getcwd()
CONFIG_FILE_PATH = BASE_PATH + "/config/config.ini"



def initiate_node(*args):
    load_configs()
    set_my_node()

    print("Start node")
    start_node()


def start_node():
    import threading
    global listen_thread

    listen_thread = threading.Thread(target=receiver.start, args=("Listener_Thread",util.get_ip_address('en0'), 3000))
    listen_thread.start()


def stop_node():
    receiver.stop()
    global listen_thread
    listen_thread.join()


def set_my_node():
    print("Set my node")

    my_node = Node(util.get_ip_address('en0'))
    pri_key, pub_key = key.get_key()

    if (pri_key == ''):
        print("Invalid Key Info...")
        return

    node.add_node(my_node)


def list_all_node():
    print ("=== list all nodes ===")
    for n in node.get_all():
        print(n)


def list_all_transaction():
    print ("=== list all transactions ===")
    for t in transaction.get_transactions():
        print (t)


def create_block():

    diff_bits = 5;
    transactions = transaction.get_transactions()

    # transaction이 없을 경우 block을 생성하지 않음
    if (len(transactions) == 0):
        print("No transactions...")
        return

    # 내 node가 가지고 있는 마지막 블럭
    last_block = block.get_last_block()

    #transaction JSON 문자열로 변환
    transactions_str = []
    for tx in transactions:
        transactions_str.append(tx.to_json())

    # transaction 으로부터 merkle root 생성
    merkle_root = merkle_tree(transactions_str)


    # block 새로 생성
    _block = Block()

    # 마지막 블록이 있는 경우
    if last_block:

        # last bock 에 대한 정보 저장
        _block.prev_block_id = last_block.block_id
        _block.prev_block_hash = last_block.block_hash

        # 작업 증명을 위해 nonce값과 결과 생성
        _block.block_id = last_block.block_id + 1
        _block.merkle_root = merkle_root
        _block.difficulty = diff_bits

        block_header = _block.getheader_json()
        hash_result, nonce = proof_of_work(block_header, diff_bits)

        # block 정보
        _block.block_hash = hash_result
        _block.nonce = nonce
        _block.tx_list = transactions_str

        # 내 node에 block 저장
        block.append_block(_block)

        # 내 node가 가지고 있는 transaction 삭제
        transaction.remove_all()

        # 나머지 node에게 block 전송
        sender.send_to_all_node((_block.to_json()), except_my_node=True)


def list_all_block():
    for b in block.get_all_block():
        print (b)


def load_configs():
    util.load_config_file(CONFIG_FILE_PATH)

