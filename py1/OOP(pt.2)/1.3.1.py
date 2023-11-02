class Dog:
    def __init__(self, dog_breed, dog_age, dog_size, dog_nose, dog_voice):
        self.breed = dog_breed
        self.age = dog_age
        self.size = dog_size
        self.nose = dog_nose
        self.voice = dog_voice

    def Guard(self, power_of_fangs):
        self.size += power_of_fangs
        
    def Hunt(self, olfaction):
        self.nose = olfaction
    
    def Bark(self, volume_voice):
        self.voice = volume_voice


watchdog = Dog("alabay", 3, "huge", "strong", 10)
snoop_dog = Dog("cocker spaniel", 2, "small", "strong", 8)
kind_dog = Dog("golden retriever", 5, "middle", "strong", 0)

if kind_dog.breed == "golden retriever":
    print("Караул! Хозяин спасай!")



class House:
    def __init__(self, material, rooms, area):
        self.material = material
        self.rooms = rooms
        self.area = area

    def calculate_property_tax(self):
        if self.material == "wood":
            return self.area * 100
        elif self.material == "brick":
            return self.area * 150
        elif self.material == "panel":
            return self.area * 120

    def calculate_heating_cost(self):
        if self.material == "wood":
            return self.rooms * 1000
        elif self.material == "brick":
            return self.rooms * 800
        elif self.material == "panel":
            return self.rooms * 1200

wooden_house = House("wood", 4, 200)
brick_house = House("brick", 5, 250)
panel_house = House("panel", 3, 150)

print("Налог на имущество:", wooden_house.calculate_property_tax())
print("Расходы на отопление:", wooden_house.calculate_heating_cost())

print("Налог на имущество:", brick_house.calculate_property_tax())
print("Расходы на отопление:", brick_house.calculate_heating_cost())

print("Налог на имущество:", panel_house.calculate_property_tax())
print("Расходы на отопление:", panel_house.calculate_heating_cost())