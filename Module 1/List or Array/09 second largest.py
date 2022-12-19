def getSecMax(l):
  if len(l) <=1:
    return None
  lar = getmax(l)
  slar = None
  for x in l:
    if x! = lar:
      if slar == None:
        slar = x
      else:
        slar = max(slar,x)
   return slarg

def getMax(l):
  res = l[0]
  for i in range(1,len(l)):
    res = max(res,l[i])
  return res
