s1 = "geeks"
print(s1)
s2 = s1.upper()
print(s2)
s3 = s2.lower()
print(s3)
print(s1.islower())
print(s2.isupper())
s = "geeksforgeeks python course"
print(s.startwith("geeks"))
print(s.endswith("course"))
print(s.startwith("Geeks",1))
print(s.startwith("geeks",8,len(s1))

s1 = "geeks for geeks"
print(s1.split(1))
s2 = "geeks, for , geeks"
print(s2.split(","))
l = ["geeksforgeeks","python","course"]
print(" ".join(l))
print(",".join(l))

#strip operation in string

print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))
