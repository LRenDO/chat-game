# Sockets Chat Project Client
# Class: CS372 Introduction to Computer Networks
# Author: Ren Demeis-Ortiz
# Description:
# Sources for socket setup:
#           My earlier CS372 sockets project
#
#           Kurose and Ross, Computer Networking: A Top-Down Approach,
#           7th Edition,Pearson Chapter 2 Section 7
#
# Sources for looping through data on send and receive:
#           https://docs.python.org/3.4/howto/sockets.html

import socket as s
import ChatSocket as cs

def run_client(req_detail):
    print('Connecting...')
    quit_cmd = '/q'
    # Instantiate socket with type of IPv4 and TCP
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    # Connect to server and send request
    socket.connect((req_detail['host_name'], req_detail['serv_port']))
    print(f"Connected to {req_detail['host_name']} ",
          f"on port {req_detail['serv_port']}")
    print('Type /q to quit. Otherwise enter your message and press enter.')

    socket = cs.ChatSocket(socket)

    while True:
        socket.send_msg()
        if socket.get_user_input() == quit_cmd:
            break
        socket.receive_msg()
        if socket.get_response().decode() == quit_cmd:
            break
        # # Send Message
        # user_input = input('You: ')
        # message = len(user_input)
        #
        # # Source: https://www.delftstack.com/howto/python/python-leading-zeros/
        # message = f'{message:08d}'
        # message += user_input
        #
        # sent = 0
        # while sent < len(message):
        #     sent += socket.send(message.encode())
        #
        # if user_input == quit_cmd:
        #     socket.close()
        #     print('Connection closed')
        #     break

        # response = b''
        #
        # # Get Response length
        # while len(response) < 8:
        #         response += socket.recv(8-len(response))
        #
        # mess_len = int(response)
        #
        # # Get incoming message
        # response = socket.recv(1024)
        #
        # while len(response) < mess_len:
        #     response += socket.recv(1024)
        #
        # if response.decode() == quit_cmd:
        #     socket.close()
        #     print('Connection closed by other user')
        #     break
        #
        # # Print Response
        # print('Other User: ', response.decode())

    return

if __name__ == '__main__':
    request_detail = \
        {"host_name": "localhost",
         "serv_port": 2222
         }
    run_client(request_detail)

