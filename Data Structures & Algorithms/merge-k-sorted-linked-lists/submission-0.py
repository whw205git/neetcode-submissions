# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        while min_heap:
            _, index, node = heapq.heappop(min_heap)

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
            
            curr.next = node
            curr = node

        return dummy.next

