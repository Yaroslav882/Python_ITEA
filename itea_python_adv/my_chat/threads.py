# Базовый пример Python Threading
#
# Установить скрипт как исполняемый через: chmod +x threads.py

import sys
import threading

# Класс потока в стиле Python
class ThreadDemo(threading.Thread):
    def __init__(self, name, startNum):
        threading.Thread.__init__(self)

        # Установите любые переменные, которые вы хотите в своем конструкторе
        self.name = name
        self.startNum = startNum

    def run(self):
        print("Running thread '%s' starting at %d" % (self.name, self.startNum))
        i=self.startNum
        while(i < (self.startNum+10)):
            print(self.name + ", Count " + str(i))
            i=i+1
            j=0
            while(j<400000):
                j=j+1

        # Чтобы выйти из нити, просто вернитесь из run() метод


def main():
    print("Running in main()...")

    print("Launching two threads...")
    thread1 = ThreadDemo("Thread 1", 100)
    thread1.start()
    thread2 = ThreadDemo("Thread 2", 200)
    thread2.start()
    print("Launched two threads...")

    all_threads=[]
    all_threads.append(thread1)
    all_threads.append(thread2)

    print("Waiting for all threads to finish")
    for one_thread in all_threads:
        one_thread.join()
    print("All threads have finished")

    print("Exiting main()...")


if __name__ == "__main__":
    sys.exit(main())
