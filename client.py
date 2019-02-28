#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys


def receive():
  while True:
    try:
      msg = client_socket.recv(BUFSIZ).decode("utf8")
      print(msg)
    except OSError:
      break

def send(msg):
  client_socket.send(bytes(msg, "utf8"))
  if msg == "{exit}":
    client_socket.close()
    sys.exit()

HOST = "127.0.0.1"
PORT = 34000

BUFSIZ = 1024
ADDR = (HOST,PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

while True:
  message = input("> ")
  send(message)