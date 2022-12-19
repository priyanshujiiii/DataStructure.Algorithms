#Here the problem is that check whether the following list is sorted or not.

def listissorted(l):
  y = "No"
  for i in range(len(l)-1):
    if l[i]==l[i+1]:
      y = "Yes"
    else:
      y = "No"
  return "No"
