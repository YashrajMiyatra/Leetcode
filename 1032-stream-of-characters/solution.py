from collections import deque

class StreamChecker:
    """
    Optimized Stream of Characters implementation.
    
    Instead of checking all suffixes linearly or using an Aho-Corasick automaton 
    which has high memory overhead in Python, we use a Reversed Prefix Trie combined
    with a bounded `collections.deque` buffer.
    
    Because the max length of any word is 200, we clamp the deque to `maxlen=200`. 
    This automatically truncates the history, dropping memory overhead to $O(1)$ during 
    stream execution.
    """
    __slots__ = ['trie', 'stream']

    def __init__(self, words: list[str]):
        self.trie = {}
        # Building the Trie backwards
        for word in set(words):
            node = self.trie
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            # '$' marks a valid word boundary
            node['$'] = True
            
        # Deques with maxlen are heavily C-optimized in Python.
        # It automatically ejects older items, keeping memory permanently O(200).
        self.stream = deque(maxlen=200)

    def query(self, letter: str) -> bool:
        # appendleft allows us to naturally iterate from most recent to oldest
        self.stream.appendleft(letter)
        
        node = self.trie
        for char in self.stream:
            # If the char path breaks, no matching suffix exists
            if char not in node:
                return False
                
            node = node[char]
            
            # If we hit a word boundary along a valid suffix path, we found a match
            if '$' in node:
                return True
                
        return False
