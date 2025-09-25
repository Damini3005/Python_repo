fruits = ['apple', 'banana', 'cherry', 'grape']

for index,fruit in enumerate(fruits,1):
   print(index, fruit)

# -----------------#

my_dict = {num:num**2 for num in range(1,11)}
print(my_dict)

# ----------------#

random_dict = {
   'a':1,
   'b':2,
   'c':3,
   'd':4
}
my_new_dict = {k:v**2 for k,v in random_dict.items()}
print(my_new_dict)


my_new_dict_2 = {k:v**2 for k,v in random_dict.items() if v % 2 ==0}
print(my_new_dict_2)


# ---------------#
def division_fn(num1,num2):
    try:
      return num1/num2
    except (ZeroDivisionError, TypeError) as err:
       print(f'error: {err}')
print(division_fn(1,'0'))
print(division_fn(1,0))
print(division_fn(1,4))


# --------------#
person = ['Tom', 5,'male']

name, age, gender = person
print(name)
print(gender)
print(age)

#-------------------------#
def myfunction(a,b, *args):
   print(f'{a=} {b=} {args=}')

myfunction(1,2,3,4,5)   


def myfunction(a,b, **kwargs):
   print(f'{a=} {b=} {kwargs=}')

myfunction(a=1, b=2, c=3, d=4)

#---------------#
l1=[i for i in range(1,4)]
l2=[i*2 for i in range(1,4)]
l3=[i**2 for i in range(1,4)]
l4=[i for i in range (1,4) if i%2 ==1]
print(l1)
print(l2)
print(l3)
print(l4)

# -------------------#
def apply_operation(x,operation):
   return operation(x)

def add(a,b):
   return a + b
add = lambda a, b: a + b
result = add(5,3)
print(f"Using a named lambda function: add(5,3) = {result}")

def add_one_hundred(number):
   return number + 100
output1 = apply_operation(10, add_one_hundred)
print(f"Using a higher-oder function with a defined function:")
print(f"apply_operation(10, add_one_hundred) -> {output1}")
print("-" * 30)

output2 = apply_operation(10, lambda number: number + 100)


# ------------------------#
def apply_to_all(nums: list, my_func):
   return [my_func(i) for i in nums]

input_nums = [1,5,8,9]
result = apply_to_all(input_nums, lambda x:x+ 100)
print(result)


