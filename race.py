class Car:

    def __init__(self):
        self.new_or_old = self.car_neq_or_old
        self.name = self.car_name
        self.color = self.car_color
        self.speed = self.car_speed
        self.km = self.way_km

    def final_speed(self):
        if self.car_new_or_old == "old":
            self.speed = int(self.car_speed / 1.5)
            return self.speed
        else:
            self.speed = self.car_speed
            return self.speed

    def info(self):
        print(f"Car is {self.car_color}. Its max speed is {self.speed} km/h. Its name is {self.car_name}")

    def drive(self, car2: "Car"):

        res1 = self.way_km / self.speed
        res2 = car2.way_km / car2.speed

        if res1 < res2:
            return f"{self.car_name} is win!"
        elif res1 > res2:
            return f"{car2.car_name} is win"
        else:
            return f"Both are win!"

    def __str__(self):
        return f"Car is {self.car_color}. Its max speed is {self.speed} km/h. Its name is {self.car_name}"


class Porsche(Car):
    car_neq_or_old = 'new'
    car_name = "Porsche"
    car_color = "white"
    car_speed =  300
    way_km = 100


class Audi(Car):
    car_neq_or_old = 'old'
    car_name = "Audi"
    car_color = "black"
    car_speed = 200
    way_km = 100


car1 = Porsche()
car2 = Audi()


print(car1.drive(car2=car2))

