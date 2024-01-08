def numberOfWays(arr, k):
   # Write your code here
  sumcount = 0
  for i in range(0, len(arr)):
    for j in range((i+1), len(arr)):
      if (arr[i]+arr[j]) == k:
        sumcount += 1
  print(sumcount)
  return sumcount

test1 = [1,2,3,4,3]
k1 = 6

test2 = [1,5,3,3,3]
k2 = 6

numberOfWays(test1, k1)

numberOfWays(test2, k2)

