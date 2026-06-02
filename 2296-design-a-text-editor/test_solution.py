import unittest
from solution import TextEditor

class TestTextEditor(unittest.TestCase):
    def test_example(self):
        textEditor = TextEditor()
        textEditor.addText("leetcode")
        self.assertEqual(textEditor.deleteText(4), 4)
        textEditor.addText("practice")
        self.assertEqual(textEditor.cursorRight(3), "etpractice")
        self.assertEqual(textEditor.cursorLeft(8), "leet")
        self.assertEqual(textEditor.deleteText(10), 4)
        self.assertEqual(textEditor.cursorLeft(2), "")
        self.assertEqual(textEditor.cursorRight(6), "practi")

if __name__ == '__main__':
    unittest.main()
