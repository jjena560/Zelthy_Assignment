class LongestSubarray:
    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = [[float('-inf') for j in range(len(B)+1)] for i in range(len(A)+1)]
        ans = 0
        for i in range(len(memo)):
            for j in range(len(memo[0])):
                if i == 0 or j == 0:
                    memo[i][j] = 0
                elif A[i-1] == B[j-1]:
                    memo[i][j] = memo[i-1][j-1] +1
                else:
                    memo[i][j] = 0
                ans = max(ans, memo[i][j])
        
        return ans
