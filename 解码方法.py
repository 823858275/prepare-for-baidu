class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        dp=[0]*len(s)
        dp[0]=1
        if s[1] != "0":
            if int(s[0:2]) <= 26:
                dp[1]=2
            else:
                dp[1]=1
        else:
            if int(s[0:2]) <= 26:
                dp[1]=1
            else:
                return 0
        for i in range(2,len(s)):
            if s[i]!="0":
                if int(s[i-1:i+1])<=26:
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]
            else:
                if int(s[i-1:i+1])<=26:
                    dp[i]=dp[i-2]
                else:
                    return 0
        return dp[-1]
print(Solution().numDecodings("22"))