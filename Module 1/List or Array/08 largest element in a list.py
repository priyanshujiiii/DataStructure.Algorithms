def getmax(l):
  for x in l:
    for y in l:
      if y>x:
        break
      else:
        return x
    return None


#efficient solution

def getmax(l):
if not l:
return None
else:
   res = l[0]
   for i in range(1,len(len(l)):
       if l[i] > res:
          res = l[i]
    return res
