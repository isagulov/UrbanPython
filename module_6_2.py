class Vehicle:
    def __init__(self, owner, mode, color, engine_power):
        self.owner = owner
        self.__mode = mode
        self.__engine_power = engine_power
        self.__color = color
        self._COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']

    def get_model(self):
        print(f'Модель: {self.__mode}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    def __init__(self, owner, mode, engine_power, color):
        super().__init__(owner, mode, engine_power, color)
        self.__PASSENGERS_LIMIT = 5

# Текущие цвета COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()