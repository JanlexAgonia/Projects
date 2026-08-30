def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

numbers = [5, 2, 8, 1, 3]

print("Before:", numbers)

bubble_sort(numbers)

print("After:", numbers)