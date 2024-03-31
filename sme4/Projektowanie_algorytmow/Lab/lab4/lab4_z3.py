import numpy as np

zero_sum_combinations = []

def calc_combinations(ls, combination='', index=0):
    global zero_sum_combinations

    if np.sum(list(map(int, combination.split()))) == 0:
        zero_sum_combinations.append(combination[1:])

    if index == len(ls):
        return

    for i in range(index, len(ls)):
        calc_combinations(ls, combination + ' ' + str(ls[i]), i + 1)


def find_zero_sums(ls):
    global zero_sum_combinations

    calc_combinations(ls)
    zero_sum_combinations.pop(0)

    return len(zero_sum_combinations) > 0


ls = [2, 4, -2, -2]
sum = 0
print(ls)
print(find_zero_sums(ls))
print(zero_sum_combinations)
print()

zero_sum_combinations.clear()
ls = np.random.randint(-5, 5, 10)
print(ls)
print(find_zero_sums(ls))
print(zero_sum_combinations)
print()

zero_sum_combinations.clear()
ls = list(map(int, input().split()))
print(ls)
print(find_zero_sums(ls))
print(zero_sum_combinations)