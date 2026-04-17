def merge_sort(a):

    if len(a) <= 1:
        return a
    
    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left,right)

def merge(left,right):

    result = []
    l = r = 0

    while l < len(left) and r < len(right):

        if left[l] <= right[r]:
            result.append(left[l])
            l +=1

        else:
            result.append(right[r])
            r +=1

    result.extend(left[l:])
    result.extend(right[r:])

    return result

arr = [38, 27, 43, 3, 9, 82, 10]

print(merge_sort(arr))














