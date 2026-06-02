class LFUCache:
    """
    Hyper-Optimized O(1) LFU Cache leveraging native Python C-Dictionaries.
    
    Architecture:
    - **Theoretical Foundation**: Traditional LFU architectures require complex structures: either a Doubly Linked List 
      of Doubly Linked Lists (O(1)) or a Min-Heap (O(log N)). In Python, instantiating thousands of custom Node objects 
      dynamically allocates memory across the heap, triggering severe Garbage Collection stalls during the 200,000 
      operations boundary.
    - **Execution (2ms - 5ms Target)**:
      1. **Exploiting Python 3.7+ Native Dict Ordering**: Standard Python dictionaries inherently preserve insertion order. 
         This means a standard `dict` functionally behaves as an Ordered Set.
      2. **O(1) Head Popping**: To evict the Least Recently Used (LRU) item from a tied frequency bucket, we bypass 
         `OrderedDict.popitem(last=False)` (which has object overhead) and execute `k = next(iter(dict))`. This instantly 
         fetches the oldest key exactly at the C-level, achieving perfect O(1) eviction without sorting.
      3. **Zero Class Overhead**: We strip away all `Node` abstractions. Values and frequencies are packed into a raw 
         list `[value, freq]` directly inside the cache map. 
      This executes entirely inside Python's C-compiled `dict` engine, representing the physical speed limit of the language.
    """
    __slots__ = ('cap', 'min_freq', 'cache', 'freq_keys')

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.cache = {}
        # defaultdict(dict) is used to track keys at specific frequencies.
        import collections
        self.freq_keys = collections.defaultdict(dict)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # O(1) Direct List Lookup (faster than attribute lookup)
        node = self.cache[key]
        f = node[1]
        
        # O(1) Remove key from its current frequency bucket
        del self.freq_keys[f][key]
        
        # O(1) Update minimum frequency pointer if its lowest bucket was just emptied
        if not self.freq_keys[f] and self.min_freq == f:
            self.min_freq += 1
            
        # O(1) Advance frequency
        node[1] = f + 1
        self.freq_keys[f + 1][key] = None
        
        return node[0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
            
        if key in self.cache:
            node = self.cache[key]
            # Update value
            node[0] = value
            f = node[1]
            
            # O(1) Inline frequency update logic to skip Python function call overhead
            del self.freq_keys[f][key]
            if not self.freq_keys[f] and self.min_freq == f:
                self.min_freq += 1
                
            node[1] = f + 1
            self.freq_keys[f + 1][key] = None
        else:
            # O(1) Eviction Logic
            if len(self.cache) == self.cap:
                # next(iter()) fetches the oldest element inserted into the dictionary in O(1) C-time
                k = next(iter(self.freq_keys[self.min_freq]))
                del self.freq_keys[self.min_freq][k]
                del self.cache[k]
                
            # O(1) Insertion
            self.cache[key] = [value, 1]
            self.freq_keys[1][key] = None
            self.min_freq = 1
