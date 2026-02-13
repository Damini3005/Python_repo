

def my_fun(z,*args, x):
  print(args)

def any_fun(a,**k):
  print(k)
  print(a)

any_fun(z=2,b=6,a=4)