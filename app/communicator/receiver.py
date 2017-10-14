import traceback

from socket import *

from app import transaction
from app.transaction import Transaction

is_running = True

def stop():
    global is_running
    is_running = False


def start(thread_name, ip_address, port):
    import json

    addr = (ip_address, port)
    buf_size = 1024

    # 소켓 생성 및 바인딩
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(5)

    while is_running:

        # 요청이 있을경우 소켓과 송신자의 ip 주소 저장
        receive_socket, sender_ip = tcp_socket.accept()

        while is_running:
            print ("Receiving")

            # 소켓으로부터 버퍼 사이즈씩 데이터 수신
            data = receive_socket.recv(buf_size)
            try :
                # 수신된 데이터가 없는 경우
                if (len(data) == 0):
                    break

                print("data received...")

                # json 형태의 데이터를 dict 타입으로 변경
                data_json_obj = json.loads(data)

                # Transaction을 받은 경우
                if data_json_obj['type'] == 'T':
                    print ("Received transaction")
                    print (data_json_obj)

                    # dict 데이터로부터 transaction 객체 생성
                    tx = Transaction().from_json(data_json_obj)

                    # transaction 추가
                    transaction.add_transaction(tx)

                # Block 을 수신한 경우
                ##### 추가

            except:
                print("recv error...")
                traceback.print_exc()
                break

    tcp_socket.close()
    receive_socket.close()

