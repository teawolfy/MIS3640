def binary_search(my_list,x):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if x == my_list[mid]:
            return mid
        elif x < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))