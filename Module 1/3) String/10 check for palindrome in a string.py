s = input('enter a string :')
low = 0
high = len(str)-1
while low<high:
  if s[low] != s[high]:
    print("No")
    break
  low = low +1
  high = high -1
  else:
    print("yes")
#second method
s = input("enter a string:")
if s == s[::-1]:
  print("yes")
else:
  print("no")
