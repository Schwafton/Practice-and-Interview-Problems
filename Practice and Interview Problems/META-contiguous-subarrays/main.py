def count_subarrays(arr):
  # Write your code here
  precount = 0
  postcount = 0
  subcount = 1
  subcount_array = []

  for i in range(0, len(arr)):

    # number of contiguous less-thans pre
    for x in range(i-1, -1, -1):
      if arr[x] < arr[i]:
        precount += 1
      else:
        break
    # number of contiguous less-thans post
    for y in range(i+1, len(arr)):
      if arr[y] < arr[i]:
        postcount += 1
      else:
        break
    # total number of sub arrays
    subcount += precount + postcount
    # append new array
    subcount_array.append(subcount)
    precount = 0
    postcount = 0
    subcount = 1
  
  print(subcount_array)
  return subcount_array


test1 = [3, 4, 1, 6, 2]

count_subarrays(test1)

test2 = [2, 4, 7, 1, 5, 3]

count_subarrays(test2)

