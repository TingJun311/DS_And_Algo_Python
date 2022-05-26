def func(myList):

  for i in range(0, len(myList)):
    for j in range(i + 1, len(myList)):
      if myList[i] == myList[j]:
        return myList[i] 
  return 0

def hashTable(myList):
  myDict = {}
  for i in range(0, len(myList)):
    if myList[i] in myDict:
      return myList[i]
    else:
      myDict[myList[i]] = i
  return 0
  

myList = [2, 1, 1, 2, 3, 4, 5]
x = hashTable(myList)
print(x)
