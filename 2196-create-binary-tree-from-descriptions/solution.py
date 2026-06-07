from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        for parent, child, is_left in descriptions:
            # Create parent node if it doesn't exist
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            # Create child node if it doesn't exist
            if child not in nodes:
                nodes[child] = TreeNode(child)
                
            # Connect parent to child
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
                
            # Record child to identify the root later
            children.add(child)
            
        # The root is the node that has no parent (i.e. is not in children set)
        for parent, _, _ in descriptions:
            if parent not in children:
                return nodes[parent]
                
        return None
