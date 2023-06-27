#User function Template for python3

def fact(num,e=1):
        if (num <= e):
            return e
        else:
            return num * fact(num-1)

class Solution:
        def nCr(self, n, r):
        
            if (r>n):
                return 0
        
            ncr = fact(n)//(fact(n-r)*fact(r))
            return int(ncr%((10**9)+7))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends