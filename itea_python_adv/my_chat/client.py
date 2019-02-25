# Установить скрипт как исполняемый через: chmod + x client.py
# Запустить:  ./client.py <IP> <PORT>
#
# Чтобы подключиться к серверу на том же компьютере, <IP> либо 127.0.0.1, либо localhost (они имеют одинаковое значение)

import socket
import sys

def main():
    if len(sys.argv) != 3:
        print("Ошибка: мне нужны твои <IP> и <PORT>")
        sys.exit()

    ip = sys.argv[1]
    port = int(sys.argv[2])

    # Создаем TCP сокет
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Ошибка: не удалось создать сокет")
        print("Описание: " + str(msg))
        sys.exit()
    print("Подключение к серверу на " + ip + " в порту " + str(port))

    # Подключаемся к серверу
    try:
        s.connect((ip , port))
    except socket.error as msg:
        print("Ошибка: не могу установить соединение")
        print("Описание: " + str(msg))
        sys.exit()
    print("Успешное соединение")

    # Отправляем сообщение на сервер
    string_unicode = "Тигринный Лев"
    raw_bytes = bytes(string_unicode,'ascii')

    try:
        bytes_sent = s.send(raw_bytes)
    except socket.error as msg:
        print("Ошибка: send() не удалось")
        print("Описание: " + str(msg))
        sys.exit()
    print("Отправленно %d байн на сервер" % bytes_sent)

    # Закрываем сокет
    try:
        s.close()
    except socket.error as msg:
        print("Ошибка: невозможно close() сокет")
        print("Ошибка: " + str(msg))
        sys.exit()
    print("Сокеты закрыты, можно выходить")

if __name__ == "__main__":
    sys.exit(main())
