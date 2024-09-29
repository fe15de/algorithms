import random
from quicksort import quicksort

def random_list():
    lis = []
    for i in range(10):
        lis.append(random.randint(0,40))
        
    return lis

def binary_search(numbers, target):
    first = numbers[0]
    last = len(numbers) - 1
    while first <= last:
        mid = (first + last) //2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            first = mid + 1
        else:
            last = mid - 1 

    return None

def verify(index):
    if index is not None:
        print(f'target found at index {index}')
    else:
        print('target not found in list')

numbers = random_list() # not ordered list
numbers = quicksort(numbers)
result = binary_search(numbers,32)
verify(result)
print(numbers)
