class Car:

   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0

   def accelerate(self, step=10):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step

   @property
   def current_speed(self):
        return self._current_speed

   @current_speed.setter
   def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

car1 = Car(make='Skoda', model_name='Superb', top_speed='260', color='Black')

car1.accelerate(30)
print(car1.current_speed)
car1.accelerate(20)
print(car1.current_speed)
car1.accelerate(70)
print(car1.current_speed)
car1.accelerate(50)
print(car1.current_speed)
car1.accelerate(30)
print(car1.current_speed)
car1.accelerate(20)
print(car1.current_speed)
car1.accelerate(70)
print(car1.current_speed)
car1.accelerate(50)
print(car1.current_speed)
