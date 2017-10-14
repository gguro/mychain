import json

from socket import *



is_running = True

def start(thread_name, ip_address, port):
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
                print(data)
            except:
                print("recv error...")
                break

    tcp_socket.close()
    receive_socket.close()

