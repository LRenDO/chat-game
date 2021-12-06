# Socket Chat Project - Server
# Class: CS372 Introduction to Computer Networks
# Author: Ren Demeis-Ortiz
# Description: This is part of a basic client / server chat where you can open
#              a window to run server.py and one to run client.py and the
#              terminals can send text back and forth. This file is for server
#              side of the chat. It listens with port 2222. Port can be changed
#              by changing serv_port in the run_server() function. Requires
#              socket and ChatSocket modules.
#
# Sources for socket setup:
#           My earlier CS372 sockets project
#
#           Kurose and Ross, Computer Networking: A Top-Down Approach,
#           7th Edition,Pearson Chapter 2 Section 7
import socket as s
import ChatSocket as cs
import Board as b

def run_server():
    """
    Runs the server side of the client / server terminal chat.

    Waits for client to connect and initiate chat, displays client's message
    and then waits for user to input message they want to send to back to the
    client. Process repeats until either the client or server quits. '/q' is
    the command to quit and can be initiated by client or server side. Using
    this command closes the server side and the client side.

    :return:
    """
    print('Awaiting connection...')
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
    quit_cmd = conn.QUIT_CMD
    conn.set_is_server(True)

    while True:
        conn.receive_msg()
        if conn.get_response().decode() == quit_cmd:
            break
        conn.send_msg()
        if conn.get_user_input() == quit_cmd:
            break

    return

if __name__ == '__main__':
    run_server()

