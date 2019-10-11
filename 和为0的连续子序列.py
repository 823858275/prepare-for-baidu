 #dp[i] = arr[0] + arr[1] + ... + arr[i]
#如果 sum(arr[m]...arr[n]) = 0;
#那么 sum(arr[0]...arr[m-1]) = sum(arr[0]...arr[n])
#和为0的最长子序列: maxLen = n - m + 1, (dp[n] = dp[m-1])
def find(nums):
    dp=[0]*(len(nums)+1)
    cnt={0:[0]}
    max_len=0
    for i in range(len(nums)):
        dp[i+1]=dp[i]+nums[i]
        if not cnt.get(dp[i+1]):
            cnt[dp[i+1]]=[i+1]
        else:
            cnt[dp[i+1]].append(i+1)
            max_len=max(max_len,i-cnt[dp[i]][0]+1)
    return max_len
