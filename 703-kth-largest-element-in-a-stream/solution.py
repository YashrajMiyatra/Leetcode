import heapq

class KthLargest:
    """
    Optimized Kth Largest Element in a Stream.
    
    Uses Python's highly optimized Timsort in C to grab the top k elements initially,
    then strictly relies on C-implemented `heapq` methods to maintain a min-heap 
    of size k, representing the k largest elements seen so far.
    
    Memory is kept to exactly O(k). Time is O(N log N) for init, and O(log k) for adds.
    """
    __slots__ = ['k', 'heap']
    
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Timsort is exceptionally fast in Python. Sorting and slicing is 
        # faster than heapifying a massive array and popping N-k times.
        nums.sort()
        self.heap = nums[-k:] if nums else []
        # Since it was sliced from a sorted array, it's already a valid min-heap.
        # But we run heapify just in case to be perfectly safe, overhead is near 0 for size k.
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            # heapreplace is faster than heappushpop and skips pushing 
            # elements that are smaller than our kth largest.
            heapq.heapreplace(self.heap, val)
            
        return self.heap[0]
