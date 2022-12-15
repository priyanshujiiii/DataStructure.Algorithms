def getmax(l):
  for x in l:
    for y in l:
      if y>x:
        break
      else:
        return x
    return None
