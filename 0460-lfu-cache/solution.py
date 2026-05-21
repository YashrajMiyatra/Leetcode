class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Sentinel head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node) -> None:
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
        self.size += 1

    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_tail(self) -> Node | None:
        if self.size == 0:
            return None
        lru_node = self.tail.prev
        self.remove(lru_node)
        return lru_node

class LFUCache:
    """
    LFUCache implementation using a frequency map of Doubly Linked Lists and a cache Hash Map.
    
    Time Complexity:
        get: O(1) average
        put: O(1) average
        
    Space Complexity: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}        # maps key -> Node
        self.freq_map = {}     # maps freq -> DoublyLinkedList
        self.min_freq = 0

    def _update_freq(self, node: Node) -> None:
        """Increments a node's frequency, handles transition, and updates min_freq."""
        f = node.freq
        
        # Remove node from its current frequency list
        curr_list = self.freq_map[f]
        curr_list.remove(node)
        
        # If the list is now empty and it was the min_freq, increment min_freq
        if curr_list.size == 0 and f == self.min_freq:
            self.min_freq += 1
            
        # Update node frequency
        node.freq += 1
        new_freq = node.freq
        
        # Add to the new frequency list
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
            
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict Least Frequently Used (and LRU if tied) node
                lru_list = self.freq_map[self.min_freq]
                evict_node = lru_list.remove_tail()
                if evict_node:
                    del self.cache[evict_node.key]
                    
            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            
            # Start frequency is 1
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1
