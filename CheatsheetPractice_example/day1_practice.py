# # --------Type of numbers---------#
print("*"*30)
# print(type(1)) 
# # print(type(1+ '10'))  #it shows error:- TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(type(-20)) 
# print(type(1 - 20)) 
# print(type(100.0)) 
# print(type(2.10)) 
# print(type(4E2)) 
# print(type(1E10)) 

# #---------Arithmatic----------#
print("*"*30)
# print(100+10)
# print(10-5)
# print(100*2)
# print(10**3)
# print(10/3)
# print(100 // 2)
# print(10 % 3)


# #------------Basic function---------#
print("*"*30)
# print(pow(8,2))
# print(abs(-10))
# print(abs(-10.10))
# print(pow(100,0.10))
# print(round(89.193))
# print(round(5.089,2))
# print(bin(687))
# print(hex(698))

#-----------converting string into numbers------------#
print("*"*30)
# age = input("How old are you?")  
# print(age)                       
# age = int(age)                    
# print(age)                        

# pi = input("What is the value of pi?")  
# print(pi)                               
# pi = float(pi)                         
# print(pi)                               


#-----------Strings----------------#
print("*"*30)
print(type('hello'))
print(type('I\'m thirsty')) 

print(type("I'm thirsty" ))
print("hello" "\n" "world")
print("I am very happy""\t""I know about that""\t""but i am thinking its really or not""\t""i have confidence" )

print("*"*30)

print('Hey you!' [-1]) 
print('Hey you!' [0])
print('Hey you!' [1])
print('Hey you!' [2])
print('Hey you!' [3])
print('Hey you!' [4])
print('Hey you!' [5])
print('Hey you!' [6])
print('Hey you!' [7])

print("*"*30)
 
name = "Nikhil Patil"
print(name[:]) 
print(name[:1])
print(name[1:])
print(name[-1:])
print(name[-1])
print(name[3])
print(name[6])
print(name[::3])
print(name[::-2])
print(name[0:10:2])
print(name[:])

print('Hi there' +'Timmy')

print("!"*10)
print("*"*30)
print("#"*50)


# --------------Basic function--------------#
todo = len('pronounsetion')
print(todo)

# ---Basic methods----------#
# print('  I am hungry  '.strip())
# print('on an island'.strip('d'))
# print('on an island'.strip('i'))
# print('but life is good!'.split())
# print('Help me'.replace('me','you'))
# print('Its Need me'.replace('me','you'))
# print('Need to make fire'.startswith('make'))
# print('Need to make fire'.startswith('Need'))
# print('and cook rice'.endswith("rice"))
# print('bye bye'.index("y"))
# print('bye bye'.index("b"))
# print('still there?'.upper())
# print("I AM HAPPY".lower())
# print('ok, i am done.'.capitalize())
# print('oh hi there'.find('e'))
# print('oh hi there'.find('r'))
# print('oh hi there'.find('h'))
# print('oh hi there'.count("h"))
# print('oh hi there'.count("e"))


# ----------String Formating----------#
print('*'*30)
name1="damini"
name2="sonali"
print(f"Hello there {name1} and {name2}")
print("Hello there %s and %s " %(name1, name2))

num1=10
num2=20
print(f"{name1} give me %d rs and {name2} give me %d rs" %(num1,num2))

wnum1=42.21
wnum2=50.52
print(f"1'st person weight is %f and 2'nd person weight is %f" %(wnum1, wnum2))

# ---------Palindrome check------------#
print('*'*25)
word = 'reviver'
p = bool(word.find(word[::-1])+1)
print(p)

# -------------Boolean------------#
print(bool(True))
print(bool(False))

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool([0]))
print(bool([1]))
print(bool({}))
print(bool({0}))
print(bool({1}))
print(bool(()))
print(bool((0)))
print(bool((1)))
print(bool(''))
print(bool('1'))
print(bool('0'))
print(bool(range(0)))
print(bool(range(1)))
print(bool(set()))
# print(bool(set(0)))
print(bool(set()))


# -----------------Lists---------------#
my_list = [1,2,'3', True]
print(len(my_list))
print(my_list.index('3'))
print(my_list.index(True))
print(my_list.count(2)) # 1 --> count how many times 2 appears
print(my_list.count('3'))
print(my_list[3])
print(my_list[1:])
print(my_list[:1])
print(my_list[-1])
print(my_list[::1])
print(my_list[0:3:1]) # : is called slicing and has the format [ start : end : step ]

# Add to list
print(my_list*2)
print(my_list + ['name'])
print(my_list + [100])  # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
print(my_list.append(100)) # None --> Mutates original list to [1, 2, '3', True,100] # Or: <list> += [<el>]

print(my_list.extend([100,200]))  # None --> Mutates original list to [1, 2, '3', True,100, 200]

print(my_list.insert(2,'!!!')) # None --> [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.
print(' '.join(['Hello','there']))

# copy a lists
basket = ['apple','pears','oranges']
print(basket)
new_basket = basket.copy()
print(new_basket)
new_basket2 = basket[:]
print(new_basket2)

# Remove from list
print([1,2,3].pop()) # 3 --> mutates original list, default index in the pop method is -1 (the last item)

print([1,2,3].pop(0))
print([1,2,3].remove(2))  #None --> [1,3] Removes first occurrence of item or raises valueError
print([1,2,3].clear())
my_list2=[2,3,5,8]
del my_list2 [0] 


# Ordering
print([1,2,5,7].sort())   # None --> Mutates list to [1, 2, 3, 5]
print([1,2,3,4].sort(reverse=True))  # None --> Mutates list to [5, 3, 2, 1]
print([1,2,3,4].reverse())  # None --> Mutates list to [3, 5, 2, 1]
print(sorted([1,2,5,3,8,2,4,6]))
print(list(reversed([1,2,3,5,4,7])))

# useful operations
print(1 in [1,2,5,3])
print(min([0.5,1,2,3,4,5]))
print(max([1,2,3,4,5,10]))
print(sum([2,4,5,7]))

# Get first and last element of a list
mlist = [63,21,30,45,82,77,98,10]
print(mlist)
first, *x, last = mlist
print(first)
print(last)

# ---------Matrix----------
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[2][0])
print(matrix[1][0])
print(matrix[2][2])
print(matrix[1][1])
print(matrix[1][2])
print(matrix[0][1])

# -----Looping through a matrix by rows---
mx = [[1,2,3], [4,5,6]]
for row in range(len(mx)):
  for col in range(len(mx[0])):
    print(mx[row][col])

# new_mylist = []
my_list1=[mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))]

# print(new_mylist.append(my_list1))
# List comprehensions
# print(new_list[<action> for <item> in <iterator> if <some conditions>])
a = [i for i in 'hello']
print(a)
b = [i*2 for i in [1,2,3]]
print(b)
c = [i for i in range(0,10) if i % 2 == 0]
print(c)

# Advanced Functions 
list_of_char= list('Helloooo')
print(list_of_char)
sum_of_elements = sum([1,2,3,4,5])
print(sum_of_elements)
element_sum = [sum(pair) for  pair in zip([1,2,3],[4,2,5])]
print(element_sum)
sorted_by_second = sorted(['hi', 'you','man'], key=lambda el: el[0])
print(sorted_by_second)
sorted_by_key = sorted([
  {'name': 'bina', 'age': 30},
  {'name':'Andy','age':18},
  {'name':'Zoey','age':55}],
  key=lambda el:(el['name']))
print(sorted_by_key)

# Read line of a file into a list
# with open("myfile.txt") as f:
#     lines = [line.strip() for line in f]
# print(lines)


# ---------Dictionaries---------
my_dict = {'name': 'andrei neagoie', 'age': 30, 'magic_power': False}
print(my_dict['name'])
print(len(my_dict))
print(list(my_dict.values()))
print(list(my_dict.items()))
my_dict['Favourite_snack'] = 'Grapes'
print(my_dict)
print(my_dict.get('age'))
print(my_dict.get('ages',0))
print(my_dict.get('ages',1))
del my_dict['name']
print(my_dict.pop('name',None))
my_dict.update({'cool':True})
print(my_dict)
print({**my_dict, **{'cool': True}})

new_dict =dict([['name','Andrei'],['age',25],['magic_power',False]])
print(new_dict)
new_dict= dict(zip(['name','age','magic_power'],['saniya', 27,False]))
print(new_dict)
new_dict1 = my_dict.pop('magic_power')
print(new_dict1)

# Dictionary Comprehension
abc ={key: value for key, value in new_dict.items() if key == 'age' or key == 'name'} 
print(abc)

# ---------Tuple------------
my_tuple = ('apple', 'grapes','mango', 'grapes')
print(my_tuple)
apple, grapes, mango, grapes = my_tuple
print(my_tuple)
print(len(my_tuple))
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[0])
print(my_tuple[3])

# Immutability
# my_tuple[1] = 'donuts'
# my_tuple.append('candy')

# methods
print(my_tuple.index('grapes'))
print(my_tuple.count('grapes'))

# zip
print(list(zip([1,2,3], [4,5,6])))

# unzip
z = [(1,2), (3,4), (7,8)]
unzip = lambda z: list(zip(*z))
print(unzip(z))

# --------------Sets------------------
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(100)
print(my_set)
my_set.add(100) #no duplicates
print(my_set) 

newe_list = [1,2,3,3,3,4,4,5,5,6,1,7]
print(set(newe_list))
new_set = set(newe_list)
print(new_set)
new_set.discard(100)
print(new_set)
# new_set.remove(100)
# print(new_set)
# new_set.clear()
# print(new_set)

set1 = {1,2,3}
set2 = {6,4,5}
set3 = set1.union(set2)
print(set1)
print(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set5 = set1.difference(set2)
print(set5)
set6 = set1.symmetric_difference(set2)
print(set6)
print(set1.issubset(set2))

print(set1.issuperset(set2))

print(set1.isdisjoint(set2))

# Frozenset
# <frozenset> = frozenset(<collection>)


# -----NONE----------
# None is used for absence of a value and can be used to show nothing has been assigned to an object.
type(None)
a = None
# == # equal values
# != # not equal
# > # left operand is greater than right operand
# < # left operand is less than right operand
# >= # left operand is greater than or equal to right operand
# <= # left operand is less than or equal to right operand
# <element> is <element> # check if two operands refer to same object in memory

# -------------Logical operator------------------
print(1 < 2 and 4> 1)
print(1 > 4 or 4 > 1)
print(1 is 1)
print(1 is not 5)


age1 = 20
if age1 < 13:
  print("you are a child")
elif age1 < 18:
  print("you are a teenager")
else:
  print("You are an adult")   

# -----------------Loops------------------
my_list1 = [1,2,3]
my_tuple1 = (1,2,3)
my_list3 = [(1,2), (3,4), (5,6)]
my_dict1 = {'a':1, 'b':2, 'c':3}

for num in my_list1:
  print(num)

for num in my_tuple1:
  print(num)

for num in my_list3:
  print(num)

for num in '123':
  print(num)

for k,v in my_dict1.items():
  print(k)
  print(v)

# msg = ''
# while msg != 'quite':
#   msg = input("what should I do?")    

#------------Range--------------
print(range(10)) 
print(range(1,10))
print(list(range(0,10,2)))


# ----Enumerate------
for i, el in enumerate('helloo'):
  print(f'{i}, {el}')

# ----------------counter ----------------
from collections import Counter 
colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
Counter = Counter(colors)
print(Counter)
Counter.most_common()[0]

# -------------Named Tuple-------------------
# Tuple is an immutable and hashable list.
#  Named tuple is its subclass with named elements.

# from collections import namedtuple
# point = namedtuple('point','x y')
# p= point(1,y=2)
# print(p)
# print(p[0])
# print(p.x)
# print(getattr(p,'y'))
# print(p._fields)

# person = namedtuple('person','name height')
# print(person)
# person = person('Jean-Luc', 187)
# print(person)
# print(f'{person.height}')
# print('{p.height}'.format(p=person))


# # -----------------OrderdidDict--------------------
# from collections import OrderedDict
# programmers = OrderedDict()
# programmers['Tim'] = ['python','javascript']
# programmers['Sarah'] = ['C++']
# programmers['Bia'] = ['Ruby','Python','Go']

# for name, langs in programmers.items():
#   print(name + '-->')
#   for lang in langs:
#     print('\t' + lang)


# # --------------Functions------------
# def some_func(a,b,x,y,z):
#     return a+ b + x + y + z

# args = (1, 2)
# kwargs = {'x': 3, 'y': 4, 'z': 5}
# result = some_func(*args, **kwargs)
# print(result) 

# def add(*a):
#   return sum(a)

# print(add(1,2,3))


# # def f(*args):
# #    return sum(args)

# # f(1,2,3,4)

# def f(x,*args):
#   print(x)
#   print(args)
# f(1,2,3,4) 

# # def my_ap(*args,z):
# #   print(args)
# # print(my_ap(1))  

# def f(x,*args,z):
#  print(args)
 
# f(1,5,z=5)  

# def f(**k):
#   print(k)
# f(a=1,b=1,c=2)  

# def f(x, **kwargs):
#   print(kwargs)
# f(x=1,b=2,c=4)  

# def f(*args,**kwargs):
#   print(args,kwargs)
# f(1,2,c=2,d=3)  

# def f(x,*args,**kwargs):
#   print(args,kwargs)
# f(1,2,3,c=3,z=4,d=6)  

# def f(*args, y, **kwargs): 
#   print(args,kwargs)
# f(2,3,y=2,d=1)     


# # ---------------Lambda--------------------
# from functools import reduce

# n=3
# fib = lambda n : n if n <= 1 else fib(n-1) + fib(n-2)
# result = fib(10)
# print(result)

# # --------------Comprehensions--------------
# list = [i+1 for i in range(10)]
# print(list)

# set ={i for i in range(10) if i > 5}
# print(set)

# # iter = (i+5 for i in range(10))
# # print(iter)

# # dict = {i: i*2 for i in range(10)}
# # print(dict)

# output = [i+j for i in range(3) for j in range(3)]
# output = []
# for i in range(3):
#   for j in range(3):
#     output.append(i+j)

# print(output)

# def my_fun(*args):
#   print(args)

# my_fun()  
# def f(*args):
#   t = 0
#   for i in args:
#     t += i

#   return t
# print(f(1,2,3,4))

# def f(**kwargs):
#   t= 0
#   for k ,v in kwargs.items():
#     t +=v
#   return t 
  
# print(f(a=1,b=2,c=5)) 

# # ------------------------Ternery condition-----------------------------------#
# # <expression_if_true> if <condition> else <expression_if_false>
# [a if a else 'zero' for a in [0,1,0,3]]

# x = 20
# result = "Even" if x % 2 == 0 else "odd"
# print(result)

# a,b = 15,20
# max = a if a > b else b
# print(max)


# # ----------Map filter reduce----------
# from functools import reduce
# print(list(map(lambda x: x+1, range(10))))
# print(list(filter(lambda x : x>5, range(10))))
# # list(reduce(lambda acc, x: acc + x, range(10)))
# result =reduce(lambda acc, x: acc + x, range(10))
# print(result)

# # -----------Any All------------#
# print(any([False,True,False])) #return true if at least one element in the iterable is truthy
# print(any([0,0,0])) #return false if iterable is empty or all are falsy
# print(any([]))       #false because its empty
# print(any([0,"",None,10])) # return true 5 is truthy

# print(all([True, 1, 3, True])) #all are truthy
# print(all([True,0,1,True]))    #0 is false so it return false
# print(all([1,'hello',[1,2]]))   #true all are truthy
# print(all([]))                   #true


# # -----examples----
# marks =[10,20,0,45,38]
# print(any(m > 35 for m in marks))

# marks1 = [45,70,89]
# print(all(m > 40 for m in marks1))


# # ---------------Closures---------------
# # A nested function references a value of its enclosing function and then the enclosing function returns the nested function
# # 1
# def get_multiplier(a):
#   def out(b):
#     return a * b
#   return out

# multiply_by_3 = get_multiplier(15.5)
# print(multiply_by_3(10))

# # 2
# def outer_fun(msg):
#   def inner_fun():
#     print(f"message: {msg}")
#   return inner_fun

# hi_msg=outer_fun("Hello")
# bye_msg=outer_fun("goodbye")  
# hi_msg()
# bye_msg()

# # 3
# def power_func(exp):
#   def power(base):
#     return base ** exp
#   return power

# square = power_func(2)
# cube = power_func(3)
# print(square(19))
# print(cube(5))

# ------------SCOPE-----------
#if varible is being assigned to anywhere in the scope , it is regarded as local variable unless it is declared as a global and nonlocal

# def get_counter():
#   i = 0
#   def out():
#     nonlocal i
#     i += 1
#     return i
#   return out

# counter = get_counter()
# print(counter())
# print(counter())
# print(counter())


# def get_counter_less():
#   i = 10
#   def less():
#     nonlocal i
#     i -= 1
#     return i
#   return less

# counter1 = get_counter_less()
# print(counter1())
# print(counter1())
# print(counter1())


# -----------------Modules---------------
# import <module_name>
# if __name__ == '__main__':
#   main()

# ---------------iterators-------------
# <iter> = iter(<collection>)

nums = [10,20,30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

# <iter> = iter{<function>, to_exclusive}
import random

rand_iter = iter(lambda: random.randint(1,10),5)
for val in rand_iter:
  print(val)

print(next(it,"done"))


# ---------------Generator-------------
def count(start, step):
  while True:
    yield start
    start += step
Counter = count(10,5)
print(next(Counter))    
print(next(Counter))    
print(next(Counter))    
print(next(Counter))    
print(next(Counter))    

#------------------- Decorators----------------
def my_decorators(func):
  def wrapper(*args,**kwargs):
    print("function is about to run...")
    result = func(*args, **kwargs)
    print("function has finished")
    return result
  return wrapper
@my_decorators
def add(a,b):
   return a + b
print(add(5,10))


# -----------Debugger Example----------------
from functools import wraps
def debug(func):
  @wraps(func)
  def out(*args,**k):
    print(func.__name__)
    return func(*args,**k)
  return out
@debug
def add(x,y):
  return x+y

print(add(10,20))


# -----------Class------------
class Name:
    age = 80

    def __init__(self, a):
        self.a = a

    @classmethod
    def get_class_name(cls):
        return cls.__name__

obj1 = Name('damini')
print(obj1.get_class_name())  

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num



# person1 = Person("Damini", 25)
# person2 = Employee("Riya", 30, "E123")

# print(person1)  
# print(person2)

# ----------------Multiple inhiritance-------------------
class A: pass
class B: pass
class C(A,B):pass
print(C.mro())

# --------------------Exception------------------
try:
   10/0
except ZeroDivisionError:
   print("No division by zero!")

while True:
   try:
      x = int(input('enter your age: '))
   except ValueError:
      print('Oops! That was no valid number. try again.....')
   else:
      print('Carry on!')
      break
# raise ValueError('some error message')


# ----------------Finally-------------------
try:
   raise KeyboardInterrupt
except:
   print('oops')
finally:
   print("All done!")   