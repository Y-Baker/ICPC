from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mapp = {_:[] for _ in range(n)}
        for one in edges:
            mapp[one[0]].append(one[1])
            mapp[one[1]].append(one[0])

        def dfs(ele, visited=set()):
            if ele == destination:
                return True
            children = mapp[ele]
            for child in children:
                if child not in visited:
                    visited.add(child)
                    if dfs(child, visited):
                        return True
            return False

        return dfs(source, set([source]))


s = Solution()
print(s.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # True
print(s.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
print(s.validPath(10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5)) # True