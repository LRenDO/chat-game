# Sockets Chat Project - ChatSocket Class
# Class: CS372 Introduction to Computer Networks
# Author: Ren Demeis-Ortiz
# Description: ChatSocket class that sends messages entered in terminal and
#              receives messages from socket and prints them to the terminal.
#              Closes socket connection on QUIT_CMD received in messages.
#
# Sources for looping through data on send and receive:
#           https://docs.python.org/3.4/howto/sockets.html
import ChatGame as cg
import random
# Todo - working on connecting chat game to this class for a game option
class ChatSocket:
    QUIT_CMD = '/q'
    PLAY_CMD = '/play'
    STOP_CMD = '/stop'

    def __init__(self, socket):
        self.socket = socket
        self.user_input = b''
        self.message = b''                      # Outgoing Message
        self.response = b''                     # Incoming Message
        self.is_server = False
        self.game_mode = False
        self.game = cg.ChatGame()

    def set_is_server(self, is_server):
        self.is_server = is_server

    def get_user_input(self):
        """
        Returns self.user_input

        :return: self.user_input
        """
        return self.user_input

    def get_response(self):
        """
        Returns self.response

        :return: self.response
        """
        return self.response

    def __input_message(self):
        """
        Prompts user to enter message and adds message length to first 8 bits.

        Uses prompt "You: " to get message from user input in terminal window.
        Processes length of input and adds it as an 8 bit prefix. E.g. 00000012
        would be added to the beginning of an input of "Hola querida" for a
        final message of 00000012Hola querida

        :return: user_input (input from the terminal)
        """

        self.user_input = input('You: ')
        if len(self.user_input) == 0:
            self.user_input = ' '

        message_len = len(self.user_input)
        # Source: https://www.delftstack.com/howto/python/python-leading-zeros/
        message_len = f'{message_len:08d}'
        self.message = message_len + self.user_input
        return self.user_input

    def send_msg(self):
        """
        Gets message from user using __input_message() and sends message.

        Closes connection if user enters QUIT_CMD
        :return: nothing
        """
        # Get Message Input
        self.user_input = self.__input_message()

        # Check for game mode
        if self.game_mode:


        elif self.user_input == self.PLAY_CMD and self.is_server:
            self.set_up_game()

        # Send Message
        sent = 0
        while sent < len(self.message):
            sent += self.socket.send(self.message.encode())
 
        if self.user_input == self.QUIT_CMD:
            self.socket.close()
            print('Connection closed')

        return

    def receive_msg(self):
        """
        Receives message, displays it, and quits if command is self.QUIT_CMD.

        Processes message length, then receives message based on length.  If
        message is self.QUIT_CMD closes socket connection.
        :return:
        """
        response_len = self.__process_length()
        # Get incoming message
        self.response = self.socket.recv(1024)

        while len(self.response) < response_len:
            self.response += self.socket.recv(1024)

        # Check for game mode
        if self.game_mode:


        elif self.response == self.PLAY_CMD and self.is_server:
            self.set_up_game()

        if self.response.decode() == self.QUIT_CMD:
            self.socket.close()
            print('Connection closed by other user')

        else:
            # Print Response
            print('Other User: ', self.response.decode())
            return

    def set_up_game(self):
        players = ['server', 'client']
        self.game_mode = True
        self.game.set_px(players[random.randrange(1)])
        self.user_input = self.game.INSTRUCTIONS
        print(self.game.INSTRUCTIONS)

    def __process_length(self):
        """
        Process the length of the received message

        :return: response_len (length of the message to be received)
        """
        # Get Response length
        response_len = b''
        while len(response_len) < 8:
            response_len += self.socket.recv(8 - len(response_len))

        return int(response_len)
