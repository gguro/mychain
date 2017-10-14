
from app import *
from app import util, key
from app.communicator import receiver, sender


listen_thread = None

def initiate_node(*args):
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
    key.generate_key()
    print("Set my node")



def create_block():
    '''
    transactions = transactions.get_transaction()

    #transaction이 없을 경우 block을 생성하지 않음
    if(len(transactions) == 0):
        return

    # 내 node가 가지고 있는 마지막 블럭
    last_block = block.get_last_block()
    '''