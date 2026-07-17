class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 1
        l,r = 0,0
        hash_map = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

        while r < len(s):
            hash_map[s[r]] = hash_map[s[r]] + 1
            freqC = max(hash_map.values())
            while ((r-l)+1 - freqC) > k:
                hash_map[s[l]] = hash_map[s[l]] - 1
                l = l + 1

            diff = (r-l)+1 - freqC
            maxLen = max(maxLen, freqC + diff)
            r = r + 1
        return maxLen
