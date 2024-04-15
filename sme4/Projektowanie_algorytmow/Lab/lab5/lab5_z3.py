def merge(left, right):
    result = []
    index_left = index_right = 0

    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
            
    result.extend(left[index_left:])
    result.extend(right[index_right:])

    return result

def merge_sort(ls):
    if len(ls) <= 1:
        return ls

    middle = len(ls) // 2
    left = ls[:middle]
    right = ls[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

ls = [6, 7, 3, 1, 4]

print(ls)
print(merge_sort(ls))