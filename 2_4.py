# Scaffold out the classes and methods for a car rental application.
class car:
    def __init__(self, type, size, cost, wheels, speed, color):
        self.type = type
        self.size = size
        self.cost = cost
        self.wheels = wheels
        self.speed = speed
        self.color = color

    def get_car_size(self):
        return self.size

    def get_car_cost(self):
        return self.cost

    def car_info(self):
        return '\nType: ' + self.type + '\nSize: ' + self.size + '\nSpeed: '+str(self.speed) + '\nColor: ' + self.color + '\nCost: $' + str(self.cost) + '\nWheels: ' + str(self.wheels)

    def start(self):
        print('STARTED')

    def stop(self):
        print('STOPPED')


class truck(car):
    def __init__(self, type, size, cost, wheels, speed, color, load_capacity):
        super().__init__(type, size, cost, wheels, speed, color)
        self.load_capacity = load_capacity

    def load(self):
        print('THE CARGO IS LOADED')

    def car_info(self):
        return super().car_info() + '\nLoad capacity: ' + str(self.load_capacity)


class sports_car(car):
    def __init__(self, type, size, cost, wheels, speed, color, hood):
        super().__init__(type, size, cost, wheels, speed, color)
        self.hood = hood

    def open_hood(self):
        print('HOOD OPENED')

    def car_info(self):
        return super().car_info() + '\nHood: ' + self.hood


c1 = car('sedan', 'medium', 100, 4, 200, 'black')
c2 = car('motorcycle', 'small', 70, 2, 220, 'red')
c3 = car('micro', 'small', 70, 4, 150, 'black')
c4 = truck('big truck', 'large', 200, 6, 250, 'blue', 10)
c5 = sports_car('sports car', 'medium', 200, 4,
                300, 'green', 'Steel Shaker Scoops')

cars = [c1, c2, c3, c4, c5]

# Using that model, return a list of all cars that cost less than $100.
print("\nCar's cost less than $100:")
for car in cars:
    if(car.get_car_cost() < 100):
        print(car.car_info())

# Using that model, return a list of only medium-sized cars.
print('\nMedium-sized cars:')
for car in cars:
    if(car.get_car_size() == 'medium'):
        print(car.car_info())
