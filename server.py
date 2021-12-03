# Sockets Chat Project Server
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

def run_server():
    print('Awaiting connection...')
    quit_cmd = '/q'
    # Instantiate socket with type of IPv4 and TCP, set port to be reused,
    # and bind address
    # Source for setsockopt: Project Instructions and Specifications
    serv_port = 2222
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    socket.bind(('', serv_port))

    # Start listening for requests
    socket.listen(1)
    # Open new connection with client and receive message
    conn, addr = socket.accept()
    print(f'Connected by: {addr[0]} on port {addr[1]}.')
    print('Awaiting message...')

    conn = cs.ChatSocket(conn)

    while True:
        conn.receive_msg()
        if conn.get_response().decode() == quit_cmd:
            break
        conn.send_msg()
        if conn.get_user_input() == quit_cmd:
            break

        # # Get incoming message length
        # incoming_message = b''
        # while len(incoming_message) < 8:
        #         incoming_message += conn.recv(8-len(incoming_message))
        #
        # mess_len = int(incoming_message)
        #
        # # Get incoming message
        # incoming_message = conn.recv(1024)
        #
        # while len(incoming_message) < mess_len:
        #     incoming_message += conn.recv(1024)
        #
        # if incoming_message.decode() == quit_cmd:
        #     conn.close()
        #     print("Connection closed by other user.")
        #     break
        #
        # print('Other User: ', incoming_message.decode())
        #
        # # Send Reply
        # user_input = input('You: ')
        # message = len(user_input)
        #
        # # Source: https://www.delftstack.com/howto/python/python-leading-zeros/
        # message = f'{message:08d}'
        # message += user_input
        #
        # sent = 0
        # while sent < len(message):
        #     sent += conn.send(message.encode())
        #
        # if user_input == quit_cmd:
        #     conn.close()
        #     print("Connection Closed")
        #     break
    return

if __name__ == '__main__':
    run_server()

