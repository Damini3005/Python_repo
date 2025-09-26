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

