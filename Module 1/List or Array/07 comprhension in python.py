l1 = [x for x in range(11) if x%2 ==0]
print(l1)
l2 = [x for x in range(11) if x%2 != 0]
print(l2)

#alternate codes 
l1 = []
for x in range(11):
  if x 52==0:
    l1.appendex(x)
l2 = []
for x in range(11):
  if x%2 != 0:
    l2.append(x)
    
def getSmaller(l,x):
    return [e for in l if e<x]
l = [9,15,12,3,7,11]
x = 10
print(getSmaller(l,x))
