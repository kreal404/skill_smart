class Transport:
    def __init__(self, wheels, passengers):
        self.wheels = wheels
        self.passengers = passengers

    def start(self):
        print("Начать движение")

    def stop(self):
        print("Остановиться")


class Car(Transport):
    def __init__(self, passengers):
        super().__init__(4, passengers)

    def honk(self):
        print("Посигналить")

    def park(self):
        print("Припарковаться")


class Bicycle(Transport):
    def __init__(self, passengers):
        super().__init__(2, passengers)

    def ring_bell(self):
        print("Позвонить в колокольчик")

    def rear_wheel(self):
        print("Ехать на заднем колесе")




class Dish:
    def __init__(self, material, capacity):
        self.material = material
        self.capacity = capacity

    def fill(self):
        print("Заполнить")

    def empty(self):
        print("Опустошить")


class Plate(Dish):
    def __init__(self, capacity):
        super().__init__("Керамика", capacity)

    def heat(self):
        print("Подогреть")

    def serve_food(self):
        print("Подать")


class Mug(Dish):
    def __init__(self, capacity):
        super().__init__("Фарфор", capacity)

    def pour(self):
        print("Налить")

    def drink(self):
        print("Выпить")