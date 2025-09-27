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
print([1,2,5,7].sort())