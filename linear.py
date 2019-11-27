# linear search function
def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            print(i)
            return i
    print(-1)
    return -1

# import test arr
from test_data import test_arr

# execute function
linear_search(test_arr, 66)
