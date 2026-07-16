class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        maxSubStrCount = 0
        ds = set()
        sp,ep = 0,0
        while ep < len(s):
            if s[ep] not in ds:
                ds.add(s[ep])
            else:
                while s[ep] in ds:
                    ds.remove(s[sp])
                    sp = sp + 1
                ds.add(s[ep])
                
            maxSubStrCount = max(maxSubStrCount,len(ds))
            ep = ep + 1

        return maxSubStrCount
            

