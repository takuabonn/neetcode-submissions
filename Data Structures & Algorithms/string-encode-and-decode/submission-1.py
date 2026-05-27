class Solution:
    def __init__(self):
        self.decodeMap = {}  
    def encode(self, strs: List[str]) -> str:
        st = ''.join(strs)
        self.decodeMap[st] = strs
        return st

    def decode(self, s: str) -> List[str]:
        return self.decodeMap[s]
