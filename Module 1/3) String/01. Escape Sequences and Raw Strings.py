s = 'welcome to meet Geek's course'

print(s)
#output : Invalid syntax

s = 'welcome to geek\'s couse'
print(s)

#escape sequences and raw strings
s = "Hi,\n welcome to the course"
print(s)
#output: hi, welcome to the course

s1 = "A simple\ example"
s2 = "Backslash at the end\\"
s3 = "\\n"
s4 = "\\t"

print(s1)
print(s2)
print(s3)
print(s4)

s1 = "c:\project\name.py"
s2 = r"c:\project\name.py"
#ouput:
#c:\project
#ame.py
#c:\project\name.py
