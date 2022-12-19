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

# efficient solution
def getSecMax(l):
  if len(l)<=1:
     return None
     lar = l[0]
     slar = None
  for x in l[1:]:
     if x > lar:
       slar = lar
       lar = x
     elif x! = lar:
       if slar==None or slar<x:
       slar=x
  return slar
