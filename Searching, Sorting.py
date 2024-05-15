numbers = [44, 10, 35, 2, 38, 95, 43, 52, 30, 73]

def linear_search(numbers, searchVal):
    for i in range(len(numbers)):
        if searchVal == numbers[i]:
            return True
    return False

#Worst case time complexity: O(N), Worst case space complexity: O(1)

def binary_search(numbers, searchVal):
    low = 0
    high = len(numbers)-1
    if len(numbers) % 2 == 0:
        pivot = int(len(numbers)/2)
    else:
        pivot = int(len(numbers)//2 + 1)
    if searchVal > numbers[pivot]:
        low = pivot
        if len(numbers[low:high]) % 2 == 0:
            pivot = int(len(numbers[low:high])/2)
        else:
            pivot = int(len(numbers[low:high])//2 + 1)
    elif searchVal == numbers[pivot]:
        return True
    elif searchVal < numbers[pivot]:
        high = pivot
        if len(numbers[low:high]) % 2 == 0:
            pivot = int(len(numbers[low:high])/2)
        else:
            pivot = int(len(numbers)//2 + 1)
    elif low == high:
        return False
    

#Binary search only works if the list is sorted.
#Worst case time complexity: O(log N) and worst case space complexity: O(1)

def bubble_sort(numbers):
    sorted = False
    while not sorted:
        swap = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swap = True
        if not swap:
            sorted = True
        

#Worst case time complexity: O(N**2), worst case space complexity: O(1)

def insertion_sort(numbers):
    pass

#Worst case time complexity: O(N**2), worst case space complexity: O(1)
