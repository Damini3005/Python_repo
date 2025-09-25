class reference:
  def __init__(self, name, age):
    self.name = name
    self.age  = age
  
  def __repr__(self):
    return f"{self.age}"
  
  def __add__(self, other):
    return self.age + other.age



r1 = reference('raja', 32)
r2 = reference('raju', 33)


add = r1 + r2
print(add)