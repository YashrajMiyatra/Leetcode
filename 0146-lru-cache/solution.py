class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRUCache implementation using a Doubly Linked List and a Hash Map.
    
    Time Complexity:
        get: O(1) average
        put: O(1) average
        
    Space Complexity: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # maps key -> Node
        
        # Initialize sentinel head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node) -> None:
        """Adds a node right after the dummy head (MRU position)."""
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def _remove(self, node: Node) -> None:
        """Removes an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: Node) -> None:
        """Moves a node to the MRU position (right after dummy head)."""
        self._remove(node)
        self._add(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)
            
            # Check if capacity has been exceeded
            if len(self.cache) > self.capacity:
                # Evict the least recently used node (just before dummy tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
