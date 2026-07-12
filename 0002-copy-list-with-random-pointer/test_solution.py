import unittest
from solution import Solution, Node

def build_list(data):
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (val, rand_idx) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

def extract_list(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    
    res = []
    for node in nodes:
        rand_idx = nodes.index(node.random) if node.random else None
        res.append([node.val, rand_idx])
    return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        data = [[7,None],[13,0],[11,4],[10,2],[1,0]]
        head = build_list(data)
        res_head = self.solution.copyRandomList(head)
        self.assertEqual(extract_list(res_head), data)
        self.assertNotEqual(id(head), id(res_head))

    def test_example_2(self):
        data = [[1,1],[2,1]]
        head = build_list(data)
        res_head = self.solution.copyRandomList(head)
        self.assertEqual(extract_list(res_head), data)

if __name__ == '__main__':
    unittest.main()
