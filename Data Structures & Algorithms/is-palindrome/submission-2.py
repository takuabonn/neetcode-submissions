class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = [x for x in list(s) if x.isalnum()]

        lp = 0
        rp = len(li) - 1

        while lp < rp:
            print(lp, rp)
            lpS = li[lp].lower()
            rpS = li[rp].lower()
            if lpS != rpS:
                return False
            lp += 1
            rp -= 1
        return True