class Alligator:
    biome = ["temperate freshwater swamp", "temperate freshwater marsh", "tropical freshwater swamp", "tropical freshwater marsh", "temperate freshwater river", "tropical freshwater river", "temperate brackish river", "tropical brackish river"]
    varieties = ["alligator", "alligator_man", "giant_alligator"]
    attributes = ["amphibious", "exotic_mount"]
    pet_properties = {
        "value": 650,
        "egg": True,
        "exotic_pet": True,
        "breeding": True,
        "animal_trainer": False
    }
    size = {
        "pup": 60,
        "young": 200000,
        "grown_up": 400000
    }
    age = {
        "grown_up": 1,
        "max": 100
    }
    meat_industry = {
        "edible_parts": {"meat": 18, "fat": 17, "brain": 1, "gizzard": 1, "heart": 1, "lung": 2, "intestines": 1, "liver": 1, "kidney": 2, "tripe": 1, "sweetbread": 1, "eye": 2, "spleen": 1}, 
        "raw_materials_and_supplies": {"bones": 21, "skull": 1, "skin": "flake", "gizzard_stone": 1}
    }

alligator = Alligator()
alligator_man = Alligator()
giant_alligator = Alligator()

alligator_man.size = 35.3
giant_alligator.size = 490

print(alligator.attributes, alligator_man.pet_properties["animal_trainer"], giant_alligator.size, alligator.age, giant_alligator.meat_industry["edible_parts"]["meat"])



class Blue_shark:
    biome = "ocean"
    attributes = "aquatic"
    tamed = False
    size = {
        "pup": 10000,
        "young": 100000,
        "grown_up": 300000
    }
    age = {
        "grown_up": 1,
        "max": 30
    }
    meat_industry = {
        "edible_parts": {"meat": 11, "fat": 8, "brain": 1, "heart": 1, "intestines": 2, "liver": 1, "kidney": 2, "tripe": 1, "sweetbread": 1, "eye": 2, "spleen": 1}, 
        "raw_materials_and_supplies": {"skull": 1, "skin": "leather"}
    }

blue_shark = Blue_shark()
print(blue_shark.biome, blue_shark.age, blue_shark.meat_industry["raw_materials_and_supplies"]["skull"])



class Alpaca:
    biome = "domestic_animal"
    pet_properties = {
        "value": 200,
        "grazer": True,
        "milk": True,
        "shear": True,
        "breeding": True,
        "animal_trainer": False
    }
    size = {
        "pup": 7000,
        "young": 35000,
        "grown_up": 70000
    }
    age = {
        "grown_up": 1,
        "max": 20
    }
    meat_industry = {
        "edible_parts": {"meat": 12, "fat": 12, "brain": 1, "heart": 1, "lung": 2, "intestines": 1, "liver": 1, "kidney": 2, "tripe": 1, "sweetbread": 1, "eye": 2, "spleen": 1}, 
        "raw_materials_and_supplies": {"bones": 21, "skull": 1, "skin": "leather", "wool": 7}
    }

alpaca = Alpaca()
print(alpaca.pet_properties["animal_trainer"], alpaca.meat_industry["raw_materials_and_supplies"]["bones"])