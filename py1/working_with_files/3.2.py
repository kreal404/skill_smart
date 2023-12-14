import random

def sum_two_numbers(path, n1, n2):
    try:
        with open(f"{path}/{n1}.txt") as file1, \
             open(f"{path}/{n2}.txt") as file2:

            nums1 = []
            for line in file1:
                nums1.append(int(line.strip()))

            nums2 = []
            for line in file2:
                nums2.append(int(line.strip()))

        if len(nums1) != 3 or len(nums2) != 3:
            return "Ошибка: содержимое файла неполное."

        sum_nums = sum(nums1 + nums2)
        return sum_nums

    except FileNotFoundError:
        return "Ошибка: файл не найден."

    except ValueError:
        return "Ошибка: некорректные данные в файле. Ожидались только числа."
    
    finally:
        if file1:
            file1.close()
        if file2:
            file2.close()

path = "."

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)

result = sum_two_numbers(path, n1, n2)
print(f"Сумма чисел из файлов {n1}.txt и {n2}.txt: {result}")