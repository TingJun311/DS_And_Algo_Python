
# Solution
def quicksort(array,left,right):
    ln = len(array)
    if left < right:
        pivot = right
        partitionIndex = partition(array, pivot, left, right)

        quicksort(array, left, partitionIndex - 1)
        quicksort(array, partitionIndex + 1, right)
    return array

def partition(array, pivot, left, right):
    pivotValue = array[pivot]
    partitionIndex = left

    for i in range(left,right):
        if array[i] < pivotValue:
            swap(array, i, partitionIndex)
            partitionIndex += 1

    swap(array, right, partitionIndex)
    return partitionIndex

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Select first and last index as 2nd and 3rd parameters
print(quicksort(numbers, 0, len(numbers) - 1))