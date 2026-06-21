import unittest
from solution import Robot

class TestRobot(unittest.TestCase):
    def test_example_1(self):
        robot = Robot(6, 3)
        robot.step(2)
        robot.step(2)
        self.assertEqual(robot.getPos(), [4, 0])
        self.assertEqual(robot.getDir(), "East")
        robot.step(2)
        robot.step(1)
        robot.step(4)
        self.assertEqual(robot.getPos(), [1, 2])
        self.assertEqual(robot.getDir(), "West")

if __name__ == '__main__':
    unittest.main()
