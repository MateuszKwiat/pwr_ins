def find_max(ls):
    if len(ls) == 1:
        return ls[0]

    middle = len(ls) // 2
    left_max = find_max(ls[:middle])
    right_max = find_max(ls[middle:])

    return max(left_max, right_max)

def second_max(ls):
    max_val = find_max(ls)

    ls_copy = [*ls]
    ls_copy.remove(max_val)
    
    sec_max = find_max(ls_copy)

    return sec_max

def avg(ls):
    if len(ls) == 1:
        return ls[0], 1

    middle = len(ls) // 2
    left_sum, left_count = avg(ls[:middle])
    right_sum, right_count = avg(ls[middle:])

    total_sum = left_sum + right_sum
    total_count = left_count + right_count

    return total_sum, total_count

ls = [4, 12, 5, 9, 2]
print(find_max(ls))
print(second_max(ls))
s, c = avg(ls)
print(s/c)
