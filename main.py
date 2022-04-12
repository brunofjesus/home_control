from multiprocessing import Process
from time import sleep

import http_server

import chatbot


def spawn_chat_bot():
    chatbot_process = Process(target=chatbot.main, args=())
    chatbot_process.start()
    return chatbot_process


def spawn_http_server():
    http_server_process = Process(target=http_server.main, args=())
    http_server_process.start()
    return http_server_process


if __name__ == "__main__":
    http_server = spawn_http_server()
    chatbot = spawn_chat_bot()

    while True:
        if not http_server.is_alive():
            spawn_http_server()
        if not chatbot.is_alive():
            spawn_chat_bot()

        sleep(5)

