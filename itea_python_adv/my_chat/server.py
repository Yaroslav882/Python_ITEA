# Установить скрипт как исполняемый через: chmod + x client.py
# Запустить: ./server.py <PORT>

import socket
import sys

def main():
    if len(sys.argv) != 2:
        print("Ошибка: программе нужен <PORT>")
        sys.exit()
    port = int(sys.argv[1])

    # Создаем TCP сокет
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Ошибка: не удалось создать сокет")
        print("Описание: " + str(msg))
        sys.exit()

    # Привязываемся к порту
    try:
        host=''  # Привязака ко всем интерфейсам
        s.bind((host,port))
    except socket.error as msg:
        print("Ошибка: невозможно подключиться к порту %d" % port)
        print("Описание: " + str(msg))
        sys.exit()

    # Прослушка
    try:
        backlog=10
        s.listen(backlog)
    except socket.error as msg:
        print("Ошибка: невозможно listen()")
        print("Описание: " + str(msg))
        sys.exit()
    print("Прослушивание сокета привязывается к порту %d" % port)

    # Принять входящий запрос
    try:
        (client_s, client_addr) = s.accept()
    except socket.error as msg:
        print("Ошибка: невозможно accept()")
        print("Описание: " + str(msg))
        sys.exit()
    print("Принято входящее соединение от клиента")
    print("Клиент IP, Port = %s" % str(client_addr))

    # Получаем данные
    try:
        buffer_size=4096
        raw_bytes = client_s.recv(buffer_size)
    except socket.error as msg:
        print("Ошибка: невозможно recv()")
        print("Описание: " + str(msg))
        sys.exit()

    string_unicode = raw_bytes.decode('ascii')
    print("Получено %d байтов от клиента" % len(raw_bytes))
    print("Сообщения: %s" % string_unicode)

    # Закрываем сокеты
    try:
        client_s.close()
        s.close()
    except socket.error as msg:
        print("Ошибка: невозможно close() сокет")
        print("Описание: " + str(msg))
        sys.exit()
    print("Сокеты закрыты, можно выходить")

if __name__ == "__main__":
    sys.exit(main())
