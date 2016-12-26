# this is python learning lesson 3
#python version: #2.7.12/3.6
import time
import os
import math
from collections import Iterable
import platform
print ('python.version is :' + platform.python_version())

dict_test = {"dict1":1, "dict2":2, "dict3":3, "dict4":4}
for key,value in dict_test.iteritems():
    print key, ":", value

for value in dict_test.itervalues():
    print "value:", value

for i, v in enumerate(dict_test):
    print i, v

for x, y in [(1, 6), (2, 7), (3, 8), (4, 9), (5, 0)]:
    print x, y

L = []
print range(1, 11)
for i in range(1, 11):
    L.append(i * i)

print L

List_test_1 = [i * i for i in range(1, 11)]
print List_test_1

List_test_2 = [x * y for x in range(1, 11) if x % 5 == 0 for y in range(1, 11) if y % 2 == 0]
print List_test_2

List_test_3 = [x+y for x in "abc" for y in "ABC"]
print List_test_3

List_test_4 = [d for d in os.listdir('.')]
print List_test_4

List_test_tmp = ['Hello', 'World', 18, 'Apple', None]
List_test_5 = [s.lower() for s in List_test_tmp if isinstance(s, str)]
print List_test_5

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fib(6)

def gfib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in gfib(6):
    print n
