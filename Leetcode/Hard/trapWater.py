class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        if height == []:
            return 0
        elif len(height) < 2:
            highest = max(height)
        else:
            highest = sorted(height)[-2]
            
        for currAltitude in range(highest):
            layer =[]
            for p in height:
                if p<= currAltitude:
                    ans +=1
            sub = 0
            for p in height:
                if p<= currAltitude:
                    sub +=1
                else:
                    break
            for p in range(len(height)):
                if height[len(height)-p-1] <= currAltitude:
                    sub+=1
                else:
                    break
            ans -= sub
            
            # for p in height:
            #     if p <= currAltitude:
            #         layer.append(False)
            #     else:
            #         layer.append(True)
            # while layer[0] != True or len(layer) == 0:
            #     layer.pop(0)
            # while layer[-1] != True or len(layer) == 0:
            #     layer.pop(-1)
            # ans += layer.count(False)
        return ans 