#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
    # code here
        max = 0
        max2 = 0
        for i in arr:
            print(i)
            if i > max:
                max = i
            else:
                if max2 < max and max2 < i:
                    max2 = i
        return max2
