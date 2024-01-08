def checkDuplicatesWithinK(nums, k):
  h = set()
  for i in range(len(nums)):
    if nums[i] in h:
      print(True)
      return True
    h.add(nums[i])
    if i >= k:
      h.remove(nums[i-k])
  print(False)
  return False
  

beep = [5,3,2,7,5,3,2,4,3,5]
boop = 3
checkDuplicatesWithinK(beep, boop)