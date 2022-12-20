txt = input("enter text:")
pat = input("Enter pattern:")
pos = txt.find(pos)
while pos >= 0:
  print(pos)
  pos = txt.find(pat, pos+1)
