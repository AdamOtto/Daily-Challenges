"""
Implement the singleton pattern with a twist.
First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance
and in every odd call of getInstance(), return the second instance.
"""

class instance:
    __instance1 = None
    __instance2 = None
    __Called = False
    def __init__(self):
        if instance.__instance1 != None:
            raise Exception("Only one instance allowed.")
        else:
            instance.__instance1 = self
            instance.__instance2 = instance2()
            instance.__Called = False

    
    @staticmethod
    def getInstance():
        if instance.__Called == False:
            instance.__Called = True
            instance.__instance2.__Called = False
            return instance.__instance2
        elif instance.__instance2.__Called == False:
            instance.__Called = False
            instance.__instance2.__Called = True
            return instance.__instance1

class instance2:
    __instance2 = None
    __Called = False
    def __init__(self):
        if instance2.__instance2 != None:
            raise Exception("Only one instance allowed.")
        else:
            instance2.__instance2 = self

"""
Return something like:
<__main__.instance object at 0x7fdafe50c3d0>
<__main__.instance2 object at 0x7fdafe50c160>
<__main__.instance object at 0x7fdafe50c3d0>
<__main__.instance2 object at 0x7fdafe50c160>
"""
t = instance()
print(t)
t = instance.getInstance()
print(t)
t = instance.getInstance()
print(t)
t = instance.getInstance()
print(t)