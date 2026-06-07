import os

template = """import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        # TODO: Add specific test cases
        pass

if __name__ == '__main__':
    unittest.main()
"""

for d in os.listdir('.'):
    if os.path.isdir(d) and d[0].isdigit():
        sol_path = os.path.join(d, 'solution.py')
        test_path = os.path.join(d, 'test_solution.py')
        if os.path.exists(sol_path) and not os.path.exists(test_path):
            with open(test_path, 'w') as f:
                f.write(template)
            print(f'Created {test_path}')
