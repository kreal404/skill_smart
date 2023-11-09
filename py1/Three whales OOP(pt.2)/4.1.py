class Dish:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

class House:
    def __init__(self, house_name, dish):
        self.house_name = house_name
        self.dish = dish

    def display(self):
        return f"House: {self.house_name}\nSpecial Dish: {self.dish.name} - {self.dish.cuisine}"


dish1 = Dish("Shchi", "Russian")
dish2 = Dish("Borsch", "Ukrainian")
dish3 = Dish("Draniki", "Belarusian")

house1 = House("House 1", dish1)
house2 = House("House 2", dish2)
house3 = House("House 3", dish3)

print(house1.display())
print(house2.display())
print(house3.display())