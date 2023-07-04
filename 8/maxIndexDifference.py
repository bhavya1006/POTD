#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
	    

        right = [0] * n  # max, j
        left = [0] * n  # min, i
        left[0] = arr[0]
        right[n - 1] = arr[n - 1]
    
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1])
    
        for j in range(n - 2, -1, -1):
            right[j] = max(arr[j], right[j + 1])
    
        i = 0
        j = 0
        ans = float('-inf')
        while j < n and i < n:
            if left[i] <= right[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        
        return ans
	        
	    

#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends