"""
Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
"""
import time

def jobScheduler(f, n):
    time.sleep(n * 0.001)
    f()
    
    
def sayHello ():
    print("Hello")
    

a = sayHello
b = 50
jobScheduler(a,b)