def check_sort_array(a):
    # b = a[0]
    # for i in range(1,len(a)):
    #     if a[i] > b:
    #         b = a[i]  this is my solution
    #     else: 
    #         return False
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True

ip1 = [1, 2, 3, 4, 5]
ip2 = [1, 3, 2, 4, 5]
ip3 = [5, 4, 3, 2, 1]

print(check_sort_array(ip1))
print(check_sort_array(ip2))
print(check_sort_array(ip3))
