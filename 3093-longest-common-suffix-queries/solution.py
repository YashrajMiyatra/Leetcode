class TrieNode:
    __slots__ = ['children', 'best_index']
    def __init__(self, best_index: int):
        self.children = {}
        self.best_index = best_index

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        """
        Finds the index of the string in wordsContainer that has the longest common suffix 
        with each query string.
        
        Time Complexity: O(sum(len(w)) for w in wordsContainer + sum(len(q)) for q in wordsQuery)
        Space Complexity: O(sum(len(w)) for w in wordsContainer)
        """
        root = TrieNode(-1)
        
        def update_best(node: TrieNode, idx: int, length: int):
            if node.best_index == -1:
                node.best_index = idx
            else:
                curr_best_idx = node.best_index
                curr_len = len(wordsContainer[curr_best_idx])
                if length < curr_len:
                    node.best_index = idx
                elif length == curr_len and idx < curr_best_idx:
                    node.best_index = idx
        
        # Build the Trie with reversed words
        for i, word in enumerate(wordsContainer):
            length = len(word)
            update_best(root, i, length)
            
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode(-1)
                curr = curr.children[char]
                update_best(curr, i, length)
                
        # Answer each query
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_index)
            
        return ans
