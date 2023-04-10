# Python Class and Object



class Parrot:
    # class attribute
    name = ""
    age = 0


# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")


# Python Inheritance

# base class
class Animal:
    @staticmethod
    def eat():
        print("I can eat!")

    @staticmethod
    def sleep():
        print("I can sleep!")


# derived class
class Dog(Animal):
    @staticmethod
    def bark():
        print("I can bark! Woof woof!!")


# Create object of the Dog class
# dog1 = Dog()
Dog.eat()
Dog.sleep()
Dog.bark()


# Calling members of the base class
# dog1.eat()
# dog1.sleep()
# Calling member of the derived class
# dog1.bark();


# Python Encapsulation
class Computer:

    def __init__(self):
        self.__maxprice = 800

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c.__maxprice = 9000
c.sell()

# using setter function
c.setMaxPrice(5000)
c.sell()


# Polymorphism
class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")


class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")


class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")


# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()


# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


# The super() function/keyword is used to give access to methods and properties of a parent or sibling class.

class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')


#
# Base class

# Example: Use of Inheritance in Python
class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print(self.name, self.color, self.price)


# Child class
class Car(Vehicle):

    def change_gear(self, no):
        print(self.name, 'change gear to number', no)


# Create object of Car
car = Car('BMW X1', 'Black', 35000)
car.info()
car.change_gear(5)


# Using Polymorphism in Python
class Circle:
    pi = 3.14

    def __init__(self, redius):
        self.radius = redius

    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("Area of Rectangle :", self.length * self.width)


# function
def area(shape):
    # call action
    shape.calculate_area()


# create object
cir = Circle(5)
rect = Rectangle(10, 5)

# call common function
area(cir)
area(rect)


# Encapsulation in Python
class Employee:
    def __init__(self, name, salary):
        # public member
        self.name = name
        # private member
        # not accessible outside of a class
        self.__salary = salary

    def show(self):
        print("Name is ", self.name, "and salary is", self.__salary)


emp = Employee("Jessa", 40000)
emp.show()


# OOP Example: Creating Class and Object in Python
class Employee:
    # class variables
    company_name = 'ABC Company'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.salary = salary

    # instance method
    def show(self):
        print('Employee:', self.name, self.salary, self.company_name)


# create first object
emp1 = Employee("Harry", 12000)
emp1.show()

# create second object
emp2 = Employee("Emma", 10000)
emp2.show()

#Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.
#Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes.

# Python program to define
# abstract class

from abc import ABC


class Polygon(ABC):

    # abstract method
    def sides(self):
        pass


class Triangle(Polygon):

    def sides(self):
        print("Triangle has 3 sides")


class Pentagon(Polygon):

    def sides(self):
        print("Pentagon has 5 sides")


class Hexagon(Polygon):

    def sides(self):
        print("Hexagon has 6 sides")


class square(Polygon):

    def sides(self):
        print("I have 4 sides")

    # Driver code


t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()
