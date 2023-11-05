class Dog:
    def __init__(self, dog_breed, dog_age, dog_size, dog_nose, dog_voice):
        self.__breed = dog_breed
        self.__age = dog_age
        self.__size = dog_size
        self.__nose = dog_nose
        self.__voice = dog_voice

    def __Guard(self, power_of_fangs):
        self.__size += power_of_fangs
        
    def __get_size(self):
        return self.__size

    def __Hunt(self, olfaction):
        self.__nose = olfaction
    
    def __Bark(self, volume_voice):
        self.__voice = volume_voice

kind_dog = Dog("golden retriever", 5, "middle", "strong", 0)


class House:
    def __init__(self, material, rooms, area):
        self.__material = material
        self.__rooms = rooms
        self.__area = area

    def __calculate_property_tax(self):
        if self.__material == "wood":
            return self.__area * 100
        elif self.__material == "brick":
            return self.__area * 150
        elif self.__material == "panel":
            return self.__area * 120

    def __calculate_heating_cost(self):
        if self.__material == "wood":
            return self.__rooms * 1000
        elif self.__material == "brick":
            return self.__rooms * 800
        elif self.__material == "panel":
            return self.__rooms * 1200
        
wooden_house = House("wood", 4, 200)