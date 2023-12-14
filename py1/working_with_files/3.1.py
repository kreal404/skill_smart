import random

def create_files():
    for i in range(1, 11):
        files = str(i) + ".txt"
        with open(files, "w") as file:
            for j in range(3):
                num = str(random.randint(1, 100))
                file.write(num + "\n")
        print("Файл", files, "создан.")

create_files()