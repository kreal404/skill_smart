prices = int(input("Кол-во цен: "))

for p in range(prices):
    price = int(input("Очередная цена: "))

    if p == 0:
        min_price = price
        max_price = price

    elif price < min_price:
        min_price = price

    elif price > max_price:
        max_price = price

print("Минимальная цена: ", min_price)
print("Максимальная цена: ", max_price)