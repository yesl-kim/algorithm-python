# 오답
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k==len(num): return '0'
        dp=['']*len(num)
        for i in range(k,len(num)):
            if dp[i-1]!='':
                dp[i]=dp[i-1]+num[i]
            else:
                dp[i]=str(min([int(x) for x in num[0:k+1]]))
        
        return str(int(dp[-1]))    
    

# 메모리 초과
# 0 <= num.length <= 10^5
def removeKdigits(num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k==len(num): return '0'
        dp=['1000000']*len(num)
        for i in range(k,len(num)):
            dp[i]=num[i:]
        
        def dfs(L,i,s):
            if len(s)==len(num)-k:
                dp[L]=str(min(int(dp[L+1]),int(s),int(dp[L])))
            else:
                for j in range(i+1,len(num)):
                    dfs(L,j,s+num[j])
        
        for i in range(k-1,-1,-1):
            dfs(i,i,num[i])

        print(dp)  
        return dp[0]

removeKdigits('1432219',3)