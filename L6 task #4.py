class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} gone'

    def stop(self):
        return f'{self.name} stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Current speed of town car {self.name} is {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'
        else:
            f'Current speed of work car {self.name} is {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


mini = SportCar(120, 'Yellow', 'Mini', False)
polo = TownCar(37, 'Red', 'Polo', False)
uaz = WorkCar(69, 'White', 'Uaz', True)
porsche = PoliceCar(110, 'Yellow', 'Porsche', True)

print(uaz.turn_left())
print(f'{porsche.go()} with speed exactly {porsche.show_speed()}')
print(f'Is {mini.name} a police car? {mini.is_police}')
print(porsche.police())
