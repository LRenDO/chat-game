# Sockets Chat Project ChatSocket Class
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

class ChatSocket:


    def __init__(self, socket):
        self.socket = socket
        self.quit_cmd = '/q'
        self.user_input = b''
        self.message = b''
        self.response = b''

    def get_user_input(self):
        return self.user_input

    def get_response(self):
        return self.response

    def __input_message(self):
        self.user_input = input('You: ')
        message_len = len(self.user_input)

        # Source: https://www.delftstack.com/howto/python/python-leading-zeros/
        message_len = f'{message_len:08d}'
        self.message = message_len + self.user_input
        return self.user_input

    def send_msg(self):
        # Get Message Input
        self.user_input = self.__input_message()
        
        # Send Message
        sent = 0
        while sent < len(self.message):
            sent += self.socket.send(self.message.encode())
 
        if self.user_input == self.quit_cmd:
            self.socket.close()
            print('Connection closed')

        return

    def receive_msg(self):
        response_len = self.__process_length()
        # Get incoming message
        self.response = self.socket.recv(1024)

        while len(self.response) < response_len:
            self.response += self.socket.recv(1024)

        if self.response.decode() == self.quit_cmd:
            self.socket.close()
            print('Connection closed by other user')

        else:
            # Print Response
            print('Other User: ', self.response.decode())
            return

    def __process_length(self):
        # Get Response length
        response_len = b''
        while len(response_len) < 8:
            response_len += self.socket.recv(8 - len(response_len))

        return int(response_len)