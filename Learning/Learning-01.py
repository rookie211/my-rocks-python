#this is my rocks python repository.
#python version: #2.7.12/3.6
import time
import platform
print ('python.version is :' + platform.python_version())

print("hello world")
print ('this is','my rocks','python','example')
print(100 + 200)
print (100 + 200)
print ("input over.")
#name = input("input your name:")
#print ('hello', name)
print(r'\\\\\t\\n\\\\')
print('''line 1
line 2
line 3''')
if 3 > 2:
    print("3 > 2")
if 3 < 1:
    print("3 < 1")
print(ord('A'))
print(chr(65))

# test if and int
# year = int(raw_input("input year:"))
# if year > 2000:
    # print "%s is 00 later"  % year
# elif year > 1980:
    # print "%s is 80 later" % year
# else:
    # print "%s is 80 before" % year

# test while
# while 1:
    # print "this is endless lop"
    # time.sleep(1)

# test dict/set

names = ['dict1', 'dict2', 'dict3', 'dict4']
scores = [91, 92, 93, 94]
print names
print scores

d = {'dict1':91, 'dict2':92, 'dict3':93, 'dict4':94}
print d
print d['dict2']

d["dict5"] = 95
print d

print "dict2" in d
print "dict6" in d

print d.get("dict2")
print d.get("dict6", 82)
print d

print d.pop("dict2")
print d
