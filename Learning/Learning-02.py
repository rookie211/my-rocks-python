# this is python learning lesson 2
#python version: #2.7.12/3.6
import time
import math
import platform
print ('python.version is :' + platform.python_version())

print abs(-3.4)
print cmp(2, 1)
print cmp("abc", "bcd")
print int("123")
a = abs
print a(-2)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type %s" % x)
    if x > 0 :
        print "my_abs is bigger zero, %d" % x
        return x
    elif x == 0 :
        print "my_abs is zero"
        return 0
    else :
        print "my_abs is litter zero, %d" % x
        return -x

print my_abs(3)
print my_abs(0)
print my_abs(-2)
#print my_abs("abc")


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    list_result = [nx, ny]
    return nx, ny, list_result

print move(100, 100, 60, 30)
