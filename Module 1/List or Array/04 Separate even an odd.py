def getEvenodd(l):
  even = []
  odd = []
  for x in l:
    if x%2 == 0:
      even.append(x)
    else:
      odd.append(x)
    return even,odd
