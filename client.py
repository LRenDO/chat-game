# Socket Chat Project - Client
# Class: CS372 Introduction to Computer Networks
# Author: Ren Demeis-Ortiz
# Description: This is part of a basic client / server chat where you can open
#              a window to run server.py and one to run client.py and the
#              terminals can send text back and forth. This file is for client
#              side of the chat. It connects to localhost with port 2222. If
#              needed IP address and port can be changed in the request_detail
#              before run_client() is called. Requires socket and ChatSocket
#              modules.
#
# Sources for socket setup:
#           My earlier CS372 sockets project
#
#           Kurose and Ross, Computer Networking: A Top-Down Approach,
#           7th Edition,Pearson Chapter 2 Section 7
import socket as s
import ChatSocket as cs

def run_client(req_detail):
    """
    Runs the client side of the client / server terminal chat.

    Prompts user for message to send to server, waits for a reply from server.
    '/q' is the command to quit and can be initiated by client or server side.
    Using this command closes the server side and the client side.

    :param req_detail: Dictionary with two elements. One for the server address
        and one for the server port.
        {"host_name": string of server's address,
         "serv_port": string of server's port }
    :return:
    """
    print('Connecting...')
    # Instantiate socket with type of IPv4 and TCP
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    # Connect to server and send request
    socket.connect((req_detail['host_name'], req_detail['serv_port']))
    print(f"Connected to {req_detail['host_name']} ",
          f"on port {req_detail['serv_port']}")
    print('Type /q to quit. Otherwise enter your message and press enter.')

    socket = cs.ChatSocket(socket)
    quit_cmd = socket.QUIT_CMD

    while True:
        socket.send_msg()
        if socket.get_user_input() == quit_cmd:
            break
        socket.receive_msg()
        if socket.get_response().decode() == quit_cmd:
            break

    return

if __name__ == '__main__':
    request_detail = \
        {"host_name": "localhost",
         "serv_port": 2222
         }
    run_client(request_detail)

