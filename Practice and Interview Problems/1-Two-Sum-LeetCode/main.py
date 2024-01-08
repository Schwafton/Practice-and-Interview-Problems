strs = ["shtstain","shtsake","shtsamorama"]
i = 0
prefix = ""
maxstr = max(strs, key=len)
print(maxstr)
equal = True
for i in range(0,200,1):
  for x in strs:
    if x[i] != maxstr[i]:
      equal = False
      break
  if equal == True:
    prefix += str(maxstr[i])
  else:
    break
print(prefix)