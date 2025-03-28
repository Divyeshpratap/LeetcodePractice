'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {node: []  for node in range(numCourses)}

        for node, dependency in prerequisites:
            preMap[node].append(dependency)

        visited = set()
        def dfs(node):

            if node in visited:
                return False
            if preMap[node] == []:
                return True
            visited.add(node)
            for ele in preMap[node]:
                if not dfs(ele): return False
            visited.remove(node)
            preMap[node] = []
            return True

        for ele in preMap:
            if not dfs(ele): return False
        return True
'''
Time Complexity: O(numCourses + num_edges)
Space Complexity: O(numCourses + num_edges)
'''
