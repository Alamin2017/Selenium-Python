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
