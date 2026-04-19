class Car():
    def __init__(self, started=False, speed=0):
        self.speed = speed
        self.started = started

    def start(self):
        self.started =  True
        print("Car Started, Let's ride!")

    def increase_speed(self,delta):
        if self.started:
            self.speed = self.speed + delta
            print ("Vroom!")
        else:
            print("You need to start the engine first")

    def stop(self):
        self.speed= 0

    # creating the object by making an instance of the Car() class
    c1 = Car()
    c2= Car(True)
    c3 = Car(True,50)
    c4 = Car(started= True, speed= 40)

# Python OOP ( object-orientated programming) is a programming paradigm that uses objects and classes to structure code. 

# It allows for the creation of reusable and modular code, making it easier to manage and maintain larger programs. In Python, you can define classes to create your own custom data types, and then create instances of those classes (objects) to work with them.

# Inheritance is a fundamental concept in OOP that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass).

#  This promotes code reusability and establishes a natural hierarchical relationship between classes. The child class can also override or extend the functionality of the parent class, allowing for more specific behavior while still retaining the core features of the parent class. In Python, inheritance is implemented by defining a new class that specifies the parent class in its definition.

