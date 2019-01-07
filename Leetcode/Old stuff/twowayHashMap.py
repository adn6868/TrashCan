class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strL = str.split(" ")
        if len(strL) != len(pattern):
            return False
        hashmap = {}
        i = 0
        
        for char in pattern:
            if strL[i] not in hashmap.keys():
                hashmap[strL[i]] = char
                i+=1
            elif hashmap[strL[i]] != char:
                return False
            else:
                i+=1
        
        i = 0
        hashmap ={}
        
        for char in pattern:
            if char not in hashmap.keys():
                hashmap[char] = strL[i]
                i+=1
            elif hashmap[char] != strL[i]:
                return False
            else:
                i+=1
                
        return True
                
                