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


print(alligator.biome)
print(giant_alligator.biome)

alligator.biome.append("temperate coastal swamp")

print(alligator.biome)
print(giant_alligator.biome)