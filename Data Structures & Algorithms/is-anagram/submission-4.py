class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for ch in s:
            if ch in hashMap:
                hashMap[ch]+= 1
            else:
                hashMap[ch] = 1
        
        for ch in t:
            if ch in hashMap:
                hashMap[ch]-= 1
            else:
                return False
        
        for key,val in hashMap.items():
            if val != 0:
                return False
        
        return True
        
        