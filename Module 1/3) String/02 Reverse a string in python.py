def reverse(k):
  s = ""
  for i in range(0,len(k),-1):
    s = s + k[i-1]
  return s

s = input("Enter a string")
rev = ""
for i in s:
  rev = i+rev
print(rev)

#efficient solution

print(s[::-1])
