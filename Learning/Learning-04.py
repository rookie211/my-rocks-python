# this is python learning lesson 3
#python version: #2.7.12/3.6
import functools
import time
import os
import math
from collections import Iterable
import platform
print ('python.version is :' + platform.python_version())

# test map/reduce
def f(x):
    return x * x

List_1 = range(1, 10)
print map(f, List_1)
print map(str, List_1)

def f2(x,y):
    return x + y
print reduce(f2, List_1)

def f3(x, y):
    return 10 * x + y
print reduce(f3, List_1)


List_str_1 = map(str, List_1)
List_int_1 = map(int, List_str_1)
print List_str_1
print List_int_1
print reduce(f3, List_int_1)


def str2num(s):
    def fn(x, y):
        return 10 * x + y
    return reduce(fn, map(int, s))
print str2num(map(str, List_1))
print reduce(lambda x,y: x * 10 + y, map(int, List_str_1))


List_name = ['adam', 'LISA', 'barT']
def name_style(s):
    result = ''
    for i in range(len(s)):
        if i == 0:
            result += s[0].upper()
        else :
            result += s[i].lower()
    return result
print map(name_style, List_name)


# filter
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, range(1, 10))

def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, '', 'C', '', 'D'])


#sort
List_sort_1 = range(1, 11)
def sorted_reversed(x, y):
    if x > y :
        return -1
    if x < y :
        return 1
    return 0
List_reversed = sorted(List_sort_1, sorted_reversed)
print List_reversed
print sorted(List_reversed)


# return function
List_sum_1 = range(1, 11)
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print calc_sum(*List_sum_1)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(*List_sum_1)
print f()

List_sum_2 = [1, 3, 5, 7, 9]
List_sum_3 = [2, 4, 6, 8, 10]
f2 = lazy_sum(*List_sum_2)
f3 = lazy_sum(*List_sum_3)
print f2(), f3()
print f2 == f3
f1 = f2
f4 = f3
print f1(), f4()
f1 = f3
f4 = f2
print f1(), f4()


#lambda function
f = lambda x: x * x
print f(5)


#decorator
print "decorator:"
def now():
    print "2016-12-27"
ff = now
ff()
print ff.__name__

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now_log():
    print "2016-12-27 15:47:00"

now_log()

def log_text(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log_text("execute: ")
def now_log_text():
    print '2016-12-27 17:08:00'

now_log_text()

#test functools.partial
int2 = functools.partial(int, base = 2)

print int2('10000000')
print int2('11')
