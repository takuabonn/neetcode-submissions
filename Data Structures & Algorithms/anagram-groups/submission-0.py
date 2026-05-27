class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same_str_map = {}
        for st in strs:
            key = str(sorted(list(st)))
            if key not in same_str_map:
                same_str_map[key] = []
            
            same_str_map[key].append(st)
        
        return same_str_map.values()
