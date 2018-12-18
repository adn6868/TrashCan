import sys
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [sys.maxsize]*len(times)
        prev = [None]*len(times)
        Q =[]
        for vertex in times:
            Q.append(vertex[0])
        dist[N-1] = 0
        while len(Q) != 0:
            
        # matrix = [sys.maxsize]*N
        # matrix[K-1] = 0
        # Q = [K]
        # while len(Q)!=0:
        #     cur = Q.pop(0)
        #     # sys.stdout.write(str(cur))
        #     for vertex in times:
        #         u = vertex[0]
        #         v = vertex[1]
        #         w = vertex[2]
        #         if u == cur:
        #             # sys.stdout.write(str(u))  
        #             Q.append(v)
        #             matrix[v-1] = min(matrix[v-1],matrix[u-1]+w)
        # sys.stdout.write(str(matrix)+'\n')
        # if sys.maxsize in matrix:
        #     return -1
        # else:
        #     return max(matrix)
        
        # for vertex in times:
        #     u = vertex[0]
        #     v = vertex[1]
        #     w = vertex[2]
        #     matrix[v-1] = min(matrix[v-1],matrix[u-1]+w)
        # if sys.maxsize in matrix:
        #     return -1
        # else: return max(matrix)
        
#         matrix = [sys.maxsize]*(N+1)
#         matrix[K] = 0
        
#         for vertex in times:
#             # sys.stdout.write(str(vertex)+'\n')
#             u = vertex[0]
#             v = vertex[1]
#             w = vertex[2]
#             # sys.stdout.write(str(u)+"=: \n")
#             matrix[v] = min(matrix[v],matrix[u]+w)
#         sys.stdout.write(str(matrix)+'\n')
#         matrix = matrix[1:]
#         if sys.maxsize in matrix:
#             return -1
#         else: return max(matrix)