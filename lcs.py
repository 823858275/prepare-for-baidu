#构建一个二维的表格，行列分别为两个数组
#状态转移方程dp[i][j]=0,i==0 and j==0;=dp[i-1][j-1],x=y;max(dp[i,j-1],dp[i-1][j])x!=y
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        #return dp[len(text1)][len(text2)]   #求lcs长度
        i,j=len(text1),len(text2)
        res=""
        while i>0 and j>0:
            if text1[i-1]==text2[j-1]:
                res=text1[i-1]+res
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    j-=1
                else:
                    i-=1
        return res                          #求lcs的子序列


print(Solution().longestCommonSubsequence("abcde","ace"))