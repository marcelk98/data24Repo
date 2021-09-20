class Car:
    def __init__(self, car_make, max_speed): #initizize
        self._car_make = car_make #encapsulation
        self.max_speed = max_speed
        self.current_speed = 0

    def increase_speed(self, speed_increase):
        if self.current_speed + speed_increase > self.max_speed:
            print(f"Your car cant go any quicker {self.max_speed}")
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_increase

my_car = Car("Audi", 200)

print(my_car.current_speed)

my_car.increase_speed(150)
print(my_car.current_speed)


# class vairibles need "self", dont need it for the functions variables


# my_car = Car("audi", 200) #instiantiate
#
# print(my_car.max_speed)
#
# def __function_1(self):
#     print("hidden function") #--- hides a function using __