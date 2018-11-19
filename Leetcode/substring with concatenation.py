import sys
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        L = len(words)
        l = len(words[0])
        ans = []
        for i in range(len(s)):
            if valid(s[i:i+L*l],words):
                ans.append(i)
        return ans

def valid(window,words):
    L = len(words)
    l = len(words[0])
    tmp = words.copy()
    if len(window) != l*L:
        return False
    for i in range(0,L*l,l):
        cur = window[i:i+l]
        if cur not in tmp:
            return False
        else:
            tmp.remove(cur)
    sys.stderr.write(str(tmp))
    # print(tmp)
    # print(words)
    sys.stderr.write(str(words))
    return len(tmp) == 0