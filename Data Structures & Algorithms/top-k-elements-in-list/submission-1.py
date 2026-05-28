class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freLi=[]
        cM = {}
        for num in nums:
            if num not in cM:
                cM[num]=0
            cM[num]+=1


        memo = {}
        for x in range(1, len(nums)+1):
            memo[x]=[]
        
        for num, count in cM.items():
            memo[count].append(num)

        print(memo)

        r = k
        key = len(nums)
        result = []
        while r != 0:
            li = memo[key][:r]
            result.extend(li)
            key-=1
            r -= len(li)
        return result[:k]


