class Book:
  def __init__(self,title,author,pages):
    print(f"--- __init__ called for  '{title}' ---")
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    print(f"--- __str__ called for '{self.title}' ---") 
    return f"'{self.title}' by {self.author}, {self.pages}"
  def __add__ (self,other):
    print(f"--- __add__ called for '{self.title}' ---")  
    if isinstance(other,Book):
      return self.pages + other.pages

    elif isinstance(other, int):
      return Book(self.title, self.author , self.pages + other) 
    else:
      raise TypeError(f"Unsupported operand type for +: 'Book' and '{type(other).__name__}'")  

print("Step 1: Creating two 'Book' objects. This will call __init__ for each.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("A Brief History of Time", "Stephen Hawking", 256)
print("-" * 50)

print("Step 2: Printing a book object. This will call __str__.")
print(type(book1))
print("-" * 50)
print(type(book2))
print("Step 3: Adding two book objects. This will call __add__.")
total_pages = book1 + 12
print(f"The result of book1 + book2 is: {total_pages} (Total pages)")
print("-" * 50)

# print("Step 4: Adding an integer to a book object. This also calls __add__.")
# extended_edition = book1 + 100
# print("A new book object was created by `book1 + 100`:")
# # This print statement will call the __str__ method of the new 'extended_edition' object
# print(extended_edition)
# print("-" * 50)

# # Example of what happens with an unsupported type
# try:
#     book1 + "some string"
# except TypeError as e:
#     print(f"Trying to add a string resulted in a TypeError, as expected:")
#     print(e)
