from binary_search import random_list
import numpy as np




def quicksort(vector):
    
    if  len(vector) != 0: 
        end = len(vector) - 1 
    else:
        end = len(vector)

    start = 0
    if start < end:
        right_pos = locate_pivot(vector, start, end)

        quicksort(vector[:right_pos])
        quicksort(vector[right_pos+1:])





def locate_pivot(vector, start, end):
    while start < end:
        while vector[end] >= vector[start] and start < end:
            end -= 1

        vector[start], vector[end] = vector[end], vector[start]

        while vector[start] <= vector[end] and start < end:
            start += 1

        vector[start], vector[end] = vector[end], vector[start]
    return start



test_vec = random_list() # not ordered list
test_vec = np.array(test_vec)
print(f"Nor ordered list: {test_vec}")
quicksort(test_vec)
print(f"Ordered list: {test_vec}")
