"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_map = {None: None}

        # Pass 1: create all nodes
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: create the new list
        curr = head
        while curr:
            node = node_map[curr]
            node.next = node_map[curr.next]
            node.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
        

