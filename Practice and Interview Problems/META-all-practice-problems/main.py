# ***Arrays***
# Reverse to Make Equal
# Given two arrays A and B  of length N, determine if there is a way to make A equal to B by recersing any subarrays from array B any number of times.
# Output: Return true if B can be made equal to A, else return false.
def are_they_equal(array_a, array_b):
  array_a.sort()  # sort array_a
  array_b.sort()  # sort array_b
  # if sorted arrays are equal, then their elements can be swapped any number of times to make their unsorted versions equal
  if array_a == array_b:
    return True
  else:
    return False

# Passing Yearbooks
# Given a list of integers 1 through n, in any order, the index of the next element visited is n-1.  Determine the number of indices visited before returning to the original index of n.
# Output: Return a list containing the number of traversals for each index.
def findSignatureCounts(arr):
  arr2 = []
  sigcount = 1
  for i in range(0, len(arr)):
    index = i
    nextindex = arr[i] - 1

    while (i != nextindex):
      sigcount += 1
      index = nextindex
      nextindex = arr[index] - 1

    arr2.append(sigcount)
    sigcount = 1

  return arr2

# Contiguous subarrays
# Given an array of N integers, For each index i, determine the number of contiguous subarrays that fulfill the following conditions: (1) Value at index i must be the max element, and (2) contiguous subarrays must either start from or end on index i
# Output: array where each index i contains an integer denoting max number of contiguous subarrays of arr[i]
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
    # append subcount to new array
    subcount_array.append(subcount)
    
    # reset counters
    precount = 0
    postcount = 0
    subcount = 1
  
  return subcount_array


# ***Strings***
# Rotational Cipher
def rotationalCipher(input, rotation_factor):
  # Write your code here
  cipher = ""
  
  if rotation_factor >= 10:
    num_factor = rotation_factor%10
  else:
    num_factor = rotation_factor
    
  if rotation_factor >= 26:
    alpha_factor = rotation_factor%26
  else:
    alpha_factor = rotation_factor
  
  for c in input:
    if c.isalnum():
      if c.isalpha():
        if c.islower():
          if (ord(c) + alpha_factor) > 122:
            cipher += chr(ord(c) + alpha_factor - 26)
          else:
            cipher += chr(ord(c) + alpha_factor)
        else:
          if (ord(c) + alpha_factor) > 90:
            cipher += chr(ord(c) + alpha_factor - 26)
          else:
            cipher += chr(ord(c) + alpha_factor)
      else:
        if (ord(c) + num_factor) > 57:
          cipher += chr(ord(c) + num_factor - 10)
        else:
          cipher += chr(ord(c) + num_factor)
    else:
      cipher += c
  
  return cipher
        
# Matching Pairs
# 

# Minimum Length Substrings
# Given two strings s and t, select a substring of s, rearrange the characters, and determine the min. length of the substring such that t is a substring of the selected substring.
# Output: minimum length of substring of s, or -1 if not possible.
def min_length_substring(s, t):
  # Write your code here
  char_locations = []
  for char in t:
    for i in range(0, len(s)):
      if char == s[i]:
        if i not in char_locations:
          char_locations.append(i)
          break
  char_locations.sort()
  return char_locations[-1] - char_locations[0] + 1


# ***Heaps***
# Largest Triple Products
# Given a list of n integers, compute a list output such that for each index i (between 0 and n-1 inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
# Output: List of n integers
def getLargest(sub):
  largest = 0
  for each in sub:
    if each > largest:
      largest = each
  sub.remove(largest)
  return largest

def findMaxProduct(arr):
  # Write your code here
  arr2 = []
  sub = []
  product = 1
  for i in range(0, len(arr)):
    if i < 2:
      arr2.append(-1)
    else:
      # make sub array from 0 to i
      for index in range(0, i+1):
        sub.append(arr[index])
      product = getLargest(sub) * getLargest(sub) * getLargest(sub)
      arr2.append(product)
      product = 1
  return arr2

# Magical Candy Bags
# Given an array containing number of pieces of candy in bags of candy, determine the maximum number of candies that can be eaten in k minutes, if it takes one minute to eat a bag of candy regardless of the number of candies in it, and once a bag of candies is eaten, it automatically refills with floor(n/2) candies, where n is the number of candies eaten 
#  Output: return max num of candies that can be eaten
def maxCandies(arr, k):
  # Write your code here
  candy_eaten = 0
  minute_counter = 0
  while minute_counter < k:
    # set/reset largest to zero
    largest = 0
    # find largest number of candies in a bag
    for each in arr:
      if each > largest:
        largest = each
    # replace largest with floor(largest/2)
    arr.remove(largest)
    arr.append(math.floor(largest/2))
    candy_eaten += largest
    minute_counter += 1
  # when minute_counter == k
  return candy_eaten

# Median Stream
#
import math
def findMedian(arr):
  # Write your code here
  sub = []
  medians = []
  # Find median from 0 to i for each i
  for i in range(0, len(arr)):
  # Make sub array from 0 to i for each i
    for x in range(0, i):
      sub.append(arr[x])
  # Sort sub array
    sub.sort()
  # if len(sub) is odd, median = sub[(len(sub) - 1)/2]
    if len(sub)%2 != 0:
      median = sub[(len(sub) - 1)/2]
  # if len(sub) is even
    else:
      lower = math.floor((len(sub) - 1)/2)
      upper = math.ceil((len(sub) - 1)/2)
      median = (sub[lower] + sub[upper])/2
    medians.append(median)
    sub.clear()
  return medians

# ***Greedy algorithms***
# Slow Sums
def getLargest2(arr):
  largest = 0
  for element in arr:
    if  element > largest:
      largest = element
  arr.remove(largest)
  return largest

def getTotalTime(arr):
  # Write your code here
  penalties = 0
  # Repeat until there is one element remaining
  while len(arr) > 1:
    # Get two largest elements and append their sum
    sum = getLargest2(arr) + getLargest2(arr)
    arr.append(sum)
    # add their sum to penalties
    penalties += sum
  return penalties

# Element Swapping
def findMinArray(arr, k):
  # Determine the smallest element from i of 0 to k
  smallest = arr[0]
  for i in range(1, k+1):
    if arr[i] < arr[0]:
      smallest = arr[i]
  # Remove the smallest element
  arr.remove(smallest)
  # Insert the smallest element at 0
  arr.insert(0, smallest)
  return arr

# Seating Arrangements
def minOverallAwkwardness(arr):
  # Write your code here
  awkwardness = 0
  arr2 = []   # for the least awkward seating arrangement
  # sort arr
  arr.sort()
  # determine if eve/odd number of people
  if len(arr)%2 == 0:
    # table assignments for even number of people
    for a in range(0, len(arr), 2):
      arr2.append(arr[a])
    for b in range((len(arr)-1), 0, -2):
      arr2.append(arr[b])
  else:
  # table assignments for odd number of people
    for c in range(0, len(arr), 2):
      arr2.append(arr[c])
    for d in range((len(arr)-2), 0, -2):
      arr2.append(arr[d])
  # calculate max awkwardness
  if math.fabs(arr2[-1] - arr2[0]) > awkwardness:
    awkwardness = math.fabs(arr2[-1] - arr2[0])
  for e in range(0, len(arr2)-1):
    if math.fabs(arr2[e] - arr2[e+1]) > awkwardness:
      awkwardness = math.fabs(arr2[e] - arr2[e+1])
  return awkwardness

# ***Search***
# Revenue Milestones
# Given two lists, daily revenues and revenue milestones, generate a list of days each milestone is met
def getMilestoneDays(revenues, milestones):
  # Write your code here
  met = []          # holds the days each milestone is met or False if not met
  revenue = 0       # holds running total of revenue
  
  # Fill met list with False corresponding to each milestone
  for milestone in milestones:
    met.append(False)
  
  # traverse each day in revenues list
  for day in range(0, len(revenues)):
    
    # keep a running total of revenue by adding each day's revenue to the previous total
    revenue += revenues[day]
    
    # traverse the miltstones list
    for m in range(0, len(milestones)):
      # if revenue is greater than or equal to a milestone
      if revenue >= milestones[m]:
        # and if the milestone has not already been met (False)
        if met[m] == False:
          # update met with the current day
          met[m] = day+1
      
  return met

# 1 Billion Users
# Given list of growthrates for apps, and number of users = growthrate^day, determine the number of days required for the sum of users across all apps to reach 1B
# Output: return full number of days required
def getBillionUsersDay(growthRates):
  # Write your code here
  users = 0       # keep running total of users across all apps for given day
  # With 1.0 < growthrate < 2.0 and 1 <= N <= 1000, we know tmin = 20, tmax = 2083
  
  # Iterate through each day from day 20(min) to day 2085(max)
  for day in range(20, 2085):
    # Iterate through growRates
    for rate in growthRates:
      # Calculate number of users for the day
      users += (rate**day)
    # If users is greater than or equal to 1B, return current day, else result users to zero for next day
    if math.floor(users) >= 1000000000:
      return day
    else:
      users = 0

# ***Hash tables***
# Pair Sums
def numberOfWays(arr, k):
   # Write your code here
  sumcount = 0
  for i in range(0, len(arr)):
    for j in range((i+1), len(arr)):
      if (arr[i]+arr[j]) == k:
        sumcount += 1
  return sumcount

# ***Sorting***
# Balanced Split
# Given an array of integers, some repeating, determine if the array can be split such that (1) the sum of the integers of the first partition is equal to the sum of the integers of the second partition and (2) all elements of one partition are greater than (and not equal to) the elements of the other.
# Output: return True if the array can be split as described, else return False
def balancedSplitExists(arr):
  # Write your code here
  
  # Requirements of Subsequences A and B
  # (1) sum of A elements equals sum of B elements
  # (2) all elements in A are less than all elements in B
  
  arr.sort()        # sort array
  totalA = 0        # sum of elements in A
  totalB = 0        # sum of elements in B
  canSplit = False  # return value

  # iterate through the list, each iteration representing a different place to slice the array
  
  for s in range(0, len(arr)-1):        # for each index from 0 to -1, slice
    totalA += arr[s]                    # sum elements through to slice index
    
    for t in range(len(arr)-1, s, -1):  # for each index from -1 to slice
      totalB += arr[t]                  # sum elements up to slice index
      
    if totalA == totalB:                # if sum of A equals sum of B AND
      if arr[s] < arr[s+1]:             # if element before slice < element after slice
        canSplit = True
        break
    else:
      totalB = 0
  return canSplit

# Counting Triangles
def countDistinctTriangles(arr):
  triangles = len(arr)         # number of distinct triangles
  listA = []                   # list to hold list of tuples where tuples have been converted to lists     

  for each in arr:                  # For each tuple in arr,
    aList = list(each)              # convert the tuple to a list,
    aList.sort()                    # sort that list,
    listA.append(aList)             # then append that list to a new list.
    
  for i in range(0, len(arr)-1):    # For indices from 0 to -2,
    for j in range(i+1, len(arr)):  # each proceeding index is visited,
      if listA[i] == listA[j]:      # and the "tuples" are compared.
        triangles -= 1              # If equal, subtract 1 from triangles.
  return triangles

# Given an array and a sum k
# Determine the number of pairs of elements in the array that sum to k
# Output: The number of elements that sum to k
def getSumCount(arr, k):
  sum_counter = 0   # Hold the number of pairs of elements sum to k
  # For each element in the array, 
  # to iterate through each subsequent element,
  # determine the sum of the two elements, 
  # and if the sum is equal to k, increment the counter.
  for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
      temp_sum = arr[i] + arr[j]
      if temp_sum == k:
        sum_counter += 1
  print(sum_counter)
  return sum_counter

# Given a list of people with their birth and death years, find the year with the highest population living
# Output: return year
def maxPopulation(arr):
  map2 = {}
  population = 0
  years = []
  max_population = 0
  max_year = 0

# Add every birth and death year to the dictionary as keys,
# if the year isn't already in the dictionary, set the value to zero AND
# if it's a birth year, increment by one BUT
# if it's a death year, I want to decrement by one
  for each in arr:
    map2[each[0]] = map2.get(each[0], 0)+1
    map2[each[1]] = map2.get(each[1], 0)-1

# iterate through the given list of lists
# add all values to a new list, years
# sort years (ascending)
  for each in arr:
    for year in each:
      years.append(year)
  years.sort()

# traverse sorted list of years,
# for each year in years,
# check to see if it's a key in our dictionary,
# if it is, then take the corresponding value to that key, and add it to the population
  for year in years:
    if year in map2:
      population += map2[year]
      # check to see if population exceeds current max, and update max if necessary and update corresponding year
      if population > max_population:
        max_population = population
        max_year = year

# after traversing the entire list of years, we're left with a max population value AND the year with the max population (output)
  print(max_year)
  print(map2)
  return max_year

test100 = [[1900,1910], [1901, 1934], [1900, 1999], [1940, 1940], [1930, 1955]]
maxPopulation(test100)