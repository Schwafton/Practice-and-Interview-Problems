def roman(input):
  dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
  arr = []
  for each in input:
    arr.append(dict[each])
  print(arr)
  i = 0
  sol = 0
  while i < len(arr)-1:
    if arr[i] < arr[i+1]:
      sol += (arr[i+1] - arr[i])
      i += 2
      print(sol)
      print(i)
    else:
      sol += arr[i]
      i += 1
      print(sol)
      print(i)
  sol += arr[i]
  print(sol)

roman("IXII")
    