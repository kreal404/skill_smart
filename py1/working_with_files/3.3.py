class Cat:
    def __init__(self, name, weight, purr_freq):
        self.name = name
        self.weight = weight
        self.purr_freq = purr_freq
    
    def __str__(self):
        return f'{self.name} ({self.weight} kg, {self.purr_freq} Hz)'

cats = []

try:
    with open('./cats.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            data = line.split()
            if len(data) == 3:
                name = data[0]
                try:
                    weight = float(data[1])
                    purr_freq = int(data[2])
                    cat = Cat(name, weight, purr_freq)
                    cats.append(cat)
                except ValueError:
                    print(f'Ошибка преобразования значений в строке: {line}')
            else:
                print(f'Некорректный формат строки: {line}')
except FileNotFoundError:
    print('Файл не найден')

for cat in cats:
    print(cat)