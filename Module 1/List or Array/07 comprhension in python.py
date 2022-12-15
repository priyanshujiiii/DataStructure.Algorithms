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

def getEvenOdd(l):
   even = [x for in l if x %2==0]
   odd = [x for in l if x%2 !=0]
return even,odd

l = [10,3,20,5,12]
even,odd = getEvenOdd(l)
print(even)
print(odd)

# word
s = "geekforgeeks"
l1 = [x for x in s if x in "aeiou"]
print(l1)
l2 = ["geeks","ide","cowres","gfg"]
l3 = [ x for x in l2 if x.startswith("g")]
print(l3)
l4 = [x*2 for x in range(6)]
print(l4)
