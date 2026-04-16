class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = []
        tlist = []
        for i in range(len(s)):
            slist.append(s[i])
        for i in range(len(t)):
            tlist.append(t[i])
        slist.sort()
        tlist.sort()
        if slist == tlist:
            return True
        else:
            return False