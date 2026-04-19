# Creating a python class and object
class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print('Halting')

        
car = Car()
car.increase_speed(10) # You need to start the car first
car.start() # Car started
car.increase_speed(40) # Vroom!

#Creating Multiple python objects
car1 = Car()
car2 = Car()
id(car1) # 140353303441344
id(car2) # 140353303441440

car1.start() # Car started, let's ride!
car1.increase_speed(20) # Vrooooom!
car1.speed # 20
car2.speed # 0

