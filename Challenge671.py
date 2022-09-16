"""
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked,
f itself will not be called for N milliseconds.
"""
from threading import Thread
from time import sleep

def Solution(f, N):
    lock = Lock()
    lock.acquire()
    t1 = time.start
    f()
    t2 = time.start
    sleep(N - (t1 - t2))
    lock.release()
    return

def LongFunc():
    sleep(100)
    print("All done!")


Solution(LongFunc, 500)
LongFunc()