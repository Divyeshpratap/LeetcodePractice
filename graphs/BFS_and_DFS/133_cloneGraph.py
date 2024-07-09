'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        cloneDict = {}
        q = deque()
        q.append(node)
        cloneDict[node] = Node(val = node.val)
        while q:
            ele = q.popleft()
            for neighbor in ele.neighbors:
                if neighbor not in cloneDict:
                    cloneDict[neighbor] = Node(val = neighbor.val)
                    q.append(neighbor)
                cloneDict[ele].neighbors.append(cloneDict[neighbor])

        return cloneDict[node]
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Runtime: 42 ms, faster than 47.38% of Python3 online submissions for Clone Graph.
Memory Usage: 16.9 MB, less than 58.35% of Python3 online submissions for Clone Graph.
'''
