
arr = [99,44,6,2,1,5,63,87,283,4,0]

def mergeSort(arr):
  if len(arr) == 1:
    return arr

  length = len(arr)
  mid = length // 2
  left = arr[:mid]
  right = arr[mid:]

  print('Left {}'.format(left))
  print('Right {}'.format(right))

  return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
  result = []
  leftIndex = 0
  rightIndex = 0

  while leftIndex < len(left) and rightIndex < len(right):
    if left[leftIndex] < right[rightIndex]:
      result.append(left[leftIndex])
      leftIndex += 1
    else:
      result.append(right[rightIndex])
      rightIndex += 1
      
  print(left,right)
  print( result + left[leftIndex:] + right[rightIndex:] )
  return result + left[leftIndex:] + right[rightIndex:]


x = mergeSort(arr)
print(x)