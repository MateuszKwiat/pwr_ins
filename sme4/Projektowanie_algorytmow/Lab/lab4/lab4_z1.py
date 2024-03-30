from numpy import random

def list_max(ls):
    max_elem = ls[0]

    for elem in ls:
        if elem > max_elem:
            max_elem = elem

    return max_elem

def list_second_max(ls):
    max_elem = ls[0]
    second_max_elem = ls[0]

    for i in range(len(ls) - 1):
        if ls[i + 1] > max_elem:
            max_elem = ls[i + 1]
        if ls[i] > second_max_elem and ls[i] < max_elem:
            second_max_elem = ls[i]

    if ls[len(ls) - 1] > second_max_elem and ls[len(ls) - 1] < max_elem:
        second_max_elem = ls[len(ls) - 1]

    return second_max_elem

def list_mean(ls):
    sum = 0
    count = 0

    for elem in ls:
        sum += elem
        count += 1

    return sum / count


ls = random.randint(-20, 20, 10)

print(ls)
print(list_max(ls))
print(list_second_max(ls))
print(list_mean(ls))
print()

ls = list(map(int, input().split()))

print()
print(ls)
print(list_max(ls))
print(list_second_max(ls))
print(list_mean(ls))