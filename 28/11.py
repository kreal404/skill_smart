def BigMinus(s1: str, s2: str):
    if s1 < s2:
        s1, s2 = s2, s1

    num1 = []
    for digit in s1[::-1]:
        num1.append(int(digit))

    num2 = []
    for digit in s2[::-1]:
        num2.append(int(digit))

    result = []

    borrow = 0

    for i in range(len(num2)):
        temp = num1[i] - num2[i] - borrow

        if temp < 0:
            temp += 10
            borrow = 1
        else:
            borrow = 0

        result.append(temp)

    for i in range(len(num2), len(num1)):
        temp = num1[i] - borrow

        if temp < 0:
            temp += 10
            borrow = 1
        else:
            borrow = 0

        result.append(temp)

    result = result[::-1]

    while len(result) > 1:
        if result[0] == 0:
            result.pop(0)
        else:
            break

    result_str = ''
    for digit in result:
        result_str += str(digit)
    return result_str

