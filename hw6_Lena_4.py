class Car:
    """Машина"""

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"New car: {self.name} (Color {self.color}) Police car - {self.is_police}")

    def go(self):
        print(f"{self.name}: The car began to move")

    def stop(self):
        print(f"{self.name}: The car pulled over")

    def turn(self, direction):
        print(f"{self.name}: The car turned {'left' if direction == 0 else 'right'}")

    def show_speed(self):
        print(f"{self.name}: The car speed - {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: The car speed - {self.speed} - NOO OVERSPEED!!!" \
            if self.speed > 40 else f"{self.name}: The car speed - {self.speed}" # super().show_speed()


class SportCar(Car):
    """Sport car"""

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('Police', 'White', 80)
police_car.go()