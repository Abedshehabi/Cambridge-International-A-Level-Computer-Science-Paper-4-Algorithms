numbers = [44, 10, 35, 2, 38, 95, 43, 52, 30, 73]

def linear_search(numbers, searchVal):
    for i in range(len(numbers)):
        if searchVal == numbers[i]:
            return True
    return False

#Worst case time complexity: O(N), Worst case space complexity: O(1)

def binary_search(numbers, searchVal): #returns the index or the searchVal 
    low = 0
    high = len(numbers)-1
    if numbers[0] == searchVal:
            return 0
    elif numbers[len(numbers)-1] == searchVal:
        return len(numbers)-1
    else:
        while(low <= high):
            mid = int((low+high)/2)
            if numbers[mid]==searchVal:
                return mid
            elif numbers[mid] > searchVal:
                high = mid -1
            elif numbers[mid] < searchVal:
                low = mid +1
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
    for i in range(1,len(numbers)):
        j=i
        while (j>0) and (numbers[j-1] > numbers[j]):
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            j -= 1

#Worst case time complexity: O(N**2), worst case space complexity: O(1)
