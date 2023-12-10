import random

def bubble_sort(arr):
    xchange = True
    while xchange:
        xchange = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                xchange = True

list1 = []
for i in range(10):
    list1.append(random.randint(1, 50))

print("Исходный массив: ", list1)

bubble_sort(list1)

print("Отсортированный массив: ", list1)