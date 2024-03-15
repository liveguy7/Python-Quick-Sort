
def divide(n, low, high):
  i = low - 1
  pivot = n[high]
  for j in range(low, high):
    if(n[j] <= pivot):
      i = i + 1
      n[i], n[j] = n[j], n[i]
  n[i + 1], n[high] = n[high], n[i + 1]
  return i + 1

def quickSort(n, low, high):
  if(low < high):
    pi = divide(n,low,high)
    quickSort(n,low,pi-1)
    quickSort(n,pi + 1, high)

col = [26,9,1,42,90,9,14,3,7,90]
length = len(col)

print("\nAfter Sorting...")
  
quickSort(col, 0, length-1)
for j in range(length):
  print(col[j], end=' ')





