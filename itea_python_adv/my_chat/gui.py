# Установить скрипт как исполняемый через: chmod + x client.py
# Запустить:  ./gui.py
#
# Примечание: Необходимы Tkinter пакеты, если не установлены читаем дальше
# Установить Ubuntu:   sudo apt-get install python3-tk
# Установить Windows:  pip install python-tk

import os
import sys
import tkinter
import time
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename

def main():
    print("Запускаем чат")

    # Инстанцирующий класс для чата
    ui = clientUI()

    # Запускаем чат, и зажмите CTRL-C для завершения
    try:
        ui.start()
    except KeyboardInterrupt:
        print("Зажимаем CTRL-C, чтобы закрыть чат")
        ui.eventDeleteDisplay()

    print("Выходим с чата")


class clientUI():
    def __init__(self):
        self.first_click = True;

    def start(self):
        print("Запускаем чат...")
        self.initDisplay()
        self.ui_messages.insert(tkinter.END, "Добавление сообщения в текстовое поле...\n")
        self.ui_input.insert(tkinter.END, "<Отправить сообщение>")
        self.ui_top.mainloop()
        print("Останавливаем чат...")

    def initDisplay(self):
        self.ui_top = tkinter.Tk()
        self.ui_top.wm_title("Это чат")
        self.ui_top.resizable('1','1')
        self.ui_top.protocol("WM_DELETE_WINDOW", self.eventDeleteDisplay)

        self.ui_messages = ScrolledText(
            master=self.ui_top,
            wrap=tkinter.WORD,
            width=50,
            height=25)

        self.ui_input = tkinter.Text(
            master=self.ui_top,
            wrap=tkinter.WORD,
            width=50,
            height=4)

        # Привязать <Кнопка-1> клика Entry к обработчику
        self.ui_input.bind('<Кнопка-1>', self.eventInputClick)
        self.ui_button_send = tkinter.Button(
            master=self.ui_top,
            text="Отправить",
            command=self.sendMsg)

        self.ui_button_file = tkinter.Button(
            master=self.ui_top,
            text="Файл",
            command=self.sendFile)

        # Вычисляем положение дисплея для всех объектов
        self.ui_messages.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.ui_input.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.ui_button_send.pack(side=tkinter.LEFT)
        self.ui_button_file.pack(side=tkinter.RIGHT)


    # Кнопка ОТПРАВИТЬ
    def sendMsg(self):
        msg = self.ui_input.get("0.0", tkinter.END+"-1c")
        print("Чат: Получил сообщение: '%s'" % msg)
        self.ui_messages.insert(tkinter.INSERT, "%s\n" % (msg))
        self.ui_messages.yview(tkinter.END)
        self.ui_input.delete("0.0", tkinter.END)


    # Кнопка ФАЙЛ
    def sendFile(self):
        file = askopenfilename()
        if(len(file) > 0 and os.path.isfile(file)):
            print("Чат: Выбран файл: %s" % file)
        else:
            print("Чат: Отмена")

    # Закрытие Чата
    def eventDeleteDisplay(self):
        print("Чат: Закрытие")
        self.ui_top.destroy()

    # Обработчик события
    def eventInputClick(self, event):
        if(self.first_click):
            self.ui_input.delete("0.0", tkinter.END)
            self.first_click = False;


if __name__ == "__main__":
    sys.exit(main())
