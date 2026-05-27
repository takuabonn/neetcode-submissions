class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = sorted(list(s))
        tl = sorted(list(t))

        if "".join(sl) == "".join(tl):
            return True
        return False