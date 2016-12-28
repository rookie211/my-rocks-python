# this is python learning lesson 3
#python version: #2.7.12/3.6
import types
import platform
print ('python.version is :' + platform.python_version())

class Student(object):
    __slots__ = ('name', 'score', '__name', '__score', 'age')

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.name = name
        self.score = score

    @property
    def score(self):
        return self.__score
    #@score.getter
    #def score(self):
    #    return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an inteter.')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self.__score = value
    def print_score(self):
        print "%s: %s" % (self.__name, self.__score)

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

    pass

def print_score(Student):
    print "%s: %s" % (Student.name, Student.score)

bart = Student("Bart Simpson", 98)
anyone = Student("anyone", 80)

print bart
print Student
print bart.name
print anyone.name, anyone.score

print_score(bart)
print_score(anyone)

bart.print_score()
anyone.print_score()
#print bart.__name

#OPP

#type isinstance
print type(124)
print type("abc")
print type(Student)
print type(bart)
print type(anyone)

print type(123) == types.IntType
print type(anyone) == types.ObjectType

print isinstance(anyone, Student)

#dir()
print dir(Student)
print dir(anyone)
print anyone.__sizeof__()
print anyone.__hash__()
print hasattr(anyone, 'name')
print getattr(anyone, 'name')

#advanced class using
print anyone.score
anyone.score = 81
print anyone.score

#__repr__ __str__
print Student(anyone.name, anyone.score)

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 0, 1
            for i in range( n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            L = []
            start = n.start
            stop = n.stop
            a, b = 0, 1
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

        

for i in Fib():
    print i

#__getitem__
fib_test_1 = Fib()
print fib_test_1[2]

print range(10)
print range(5,10)
print fib_test_1[2:5]
print fib_test_1[0:10]



#__getattr__
class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path
    pass

print Chain("test_path").status.user.timeline.list
chain_test = Chain("chain_test")
print chain_test.status.user.bin


#__call__
