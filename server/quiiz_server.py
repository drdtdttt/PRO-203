import socket
from threading import Thread
import random

server = socket.socket(AF_INET, socket.SOCK_STREAM)

ip_address = '137.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

print("Server has started...")

def clientthread(conn):
    score = 0
    conn.send("Welcome to this qui game!".encode('utf-8'))
    conn.send("You will receive a quetion. The answer to that quetion should be one of a, b, c or d\n".encode('utf-8'))
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index, quetion, answer = get_random_quetion_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_quetion(index)
                index, quetion, answer = get_random_quetion_answer(conn)
            else:
                remove(conn)
        except:
            continue

def get_random_quetion_answer(conn):
    random_index = randome.randint(0,len(quetions) -1)
    random_quetion = quetions[random_index]
    random_answer = answers[random_index]
    conn.send(random_quetion.encode('utf-8'))
    return random_index, random_quetion, random_answer

def remove_quetion(index):
    quetions.pop(index)
    answers.pop(index)

def remove_nickname (nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while true:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.append(nickname)
    print (nickname + " connected!")
    new_thread = Thread(target= clientthread,args=(conn,nickname))
    new_thread.start()

