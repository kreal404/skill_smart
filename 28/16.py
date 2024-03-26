def MaximumDiscount(N: int, price: list) -> int:
    price.sort(reverse=True)
    discount = 0

    for i in range(2, N, 3):
        discount += price[i]

    return discount

