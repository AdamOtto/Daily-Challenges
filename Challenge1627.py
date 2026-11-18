"""
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked,
f itself will not be called for N milliseconds.
"""
import threading
import time


def Solution(f, N):
    lock = threading.Lock()
    lock.acquire()
    t1 = time.time()
    f()
    t2 = time.time()
    sleeper(N - (t1 - t2))
    lock.release()
    return

# Wait 1 second then print ALL DONE!
def LongFunc():
    sleeper(1)
    print("All done!")

# Wait N seconds.
def sleeper(N):
    t1 = time.time()
    t2 = time.time()
    while N >= t2 - t1:
        t2 = time.time()
    return

# Lock LongFunc for 5 seconds after calling it.
Solution(LongFunc, 5)
# Call LongFunc again, should be a 5sec delay between the first and second call.
LongFunc()