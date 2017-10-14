
import threading
from socket import *

from app import node, util


def send(ip_address, message, port, *args):
    receiver_addr = (ip_address, port)
    tcp_socket = socket(AF_INET, SOCK_STREAM)

    try:
        tcp_socket.connect(receiver_addr)
        tcp_socket.send(message.encode('utf-8'))
    except:
        print ("Connection Failed while sending...", e)
        

def send_to_all_node(message, except_my_node=False):
    # node 목록에서 ip만 리스트로 추출
    nodelist = node.get_all()
    address_list = []

    for nd in nodelist:
        address_list.append(nd.ip_address)

    print (address_list)

    # except_my_node=True 일 경우 내 node를 제외한 node에게 전송
    if except_my_node:
        address_list = address_list # 나중에 수정

    send_threads = []

    for addr in address_list:
        try:
            # 메시지를 전송하는 스레드 생성 및 실행
            t = threading.Thread(target=send, kwargs={'ip_address': addr,
                                                      'message': message,
                                                      'port':3000})
            t.start()
            send_threads.append(t)
        except:
            print("SENDTOALL EXCEPT", e)

    # 스레드 객체를 배열로 저장해둔 후 동기화
    for thread in send_threads:
        thread.join()


if __name__ == '__main__':
    print ('sernder')