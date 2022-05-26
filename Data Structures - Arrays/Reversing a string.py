

def reverse (stri):
  myList = []
  for i in range( len(stri) - 1, - 1, - 1):
    myList.append(stri[i])    
  return ''.join(myList)

x = reverse('I am human')
print(x)  

# or just stri[::-1]