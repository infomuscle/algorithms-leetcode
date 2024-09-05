# 제출 코드 - Runtime 97.19 Memory 10.25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Intuition
# Level Order = left to right, level by level
# 같은 층을 같은 리스트에 담는다.
# BFS 쓰면 되는 것 같은데.
# 왜 미디엄일까
# 노드는 2000개, 값은 -1000 ~ 1000

# Approach
# BFS니깐 큐를 만들고
# while 반복을 하는데
# 2중 while이어야겠다.
# 큐의 노드를 모두 빼서, 모든 자식들을 리스트에 담아서 결과 리스트에 넣고,
# 빠진 노드의 모든 노드들은 별도로 킵해뒀다가 큐에 한번에 넣기.
from collections import deque


class Solution:
    def levelOrder(self, root):
        result = []
        # runtime 97.76 memory 55.09

        queue = deque([root])
        while queue:

            nodes_in_level = []
            while queue:
                node = queue.popleft()
                if node:
                    nodes_in_level.append(node)

            values_in_level = []
            for node in nodes_in_level:
                values_in_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(values_in_level) > 0:
                result.append(values_in_level)

        return result
