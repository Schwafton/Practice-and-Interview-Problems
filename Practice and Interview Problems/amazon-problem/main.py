def group(n):
  if n == 0:
    return 1
  else:
    return n

arr = [1,2,1,3,1,2]

arr.sort()
print(arr)

newarr = []
valarr = []
freqarr = []

valarr.append(arr[0])
freqarr.append(arr.count(arr[0]))
newarr.append([valarr[0], freqarr[0]])

for x in arr:
  for y in valarr:
    if x != y:
      valarr.append(x)
      newarr.append([x, arr.count(x)])
    
print(newarr)
