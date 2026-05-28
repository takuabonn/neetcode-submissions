class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        az = [chr(ord("a")+i) for i in range(26)]

        group = {}
        def initMap():
            countM = {}
            for ch in az:
                countM[ch] = 0
        
            return countM
        
        for st in strs:
            countM = initMap()
            for ch in st:
                countM[ch]+=1
            key = tuple(countM.values())
            if key not in group:
                group[key] = []
            group[key].append(st)
        
        result = []
        for li in group.values():
            result.append(li)
        return result

                

                

        
        
    