#User function Template for python3

def sqDig(num):
    sum = 0
    while num>0:
        temp = num%10
        sum += temp**2
        num = num//10
    return sum
    
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sqDig(num)
    return num == 1

class Solution:
    def nextHappy (self, N):
        N += 1
        while not is_happy(N):
            N += 1
        return N

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends