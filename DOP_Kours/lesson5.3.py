from time import sleep

from threading import Thread

from threading import Lock, RLock, Semaphore, BoundedSemaphore

Lock # простой mutex - потокобезопасный обьект блокировки

RLock # рекурсивный mutex, один блокировщик может заблокировать многократно

Semaphore # версия мьютекса, с ограничением по количеству блокировок

BoundedSemaphore # версия мьютекса следит за тем, что-бы количество блокировок == разблокировок


def sender(lst):
    for i in range(10):
        lock.acquire()
        lst.append(i)
        lock.release()
    lock.acquire()
    lst.append('STOP')
    lock.release()


def getter(lst):
    while True:
        if len(lst) == 0:
            sleep(0.1)
            continue
        lock.acquire()
        item = lst.pop(0)
        lock.release()
        if item == 'STOP':
            break
        print(item)


lst = []
lock = Lock()
thread1 = Thread(target=sender, args=(lst,))
thread2 = Thread(target=getter, args=(lst,))

thread1.start()
thread2.start()