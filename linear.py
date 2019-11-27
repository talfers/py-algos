# linear search function
def linear_search(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            print(i)
            return i
        i+=1
    print(-1)
    return -1

# import test arr
from test_data import test_arr

# execute function
linear_search(test_arr, 38)
