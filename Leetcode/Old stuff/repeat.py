class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap ={}
        for i in A:
            if i in hashmap:
                return i
            else:
                hashmap[i] = True
        