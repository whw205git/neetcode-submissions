class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # update access order 
            self.remove(self.cache[key])
            self.insertAtRight(self.cache[key])
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        # remove existing node
        if key in self.cache:
            self.remove(self.cache[key])

        # create new node
        self.cache[key] = Node(key, value)
        self.insertAtRight(self.cache[key])

        # Evict if over capacity
        if len(self.cache) > self.capacity:
            to_remove = self.left.next
            del self.cache[to_remove.key]
            self.remove(to_remove)

    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = node.next = None

    def insertAtRight(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = node
        node.next = next
        node.prev = prev
        next.prev = node

