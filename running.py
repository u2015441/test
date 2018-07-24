class Person:
  def __init__(self,name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("Enter your name:")
x = input()
print("Hello, " + x)

a = "Hello, World!"
b = a.split(",")
print(b[0])