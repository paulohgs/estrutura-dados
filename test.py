import unittest
from linked_list import Linked_list

class TestingList(unittest.TestCase):
    
    def test_append(self):
        list = Linked_list()
        test = list.append(9)
        self.assertEqual(True, test)

    def test_print(self):
        list = Linked_list()
        list.append(9)
        list.append(10)
        list.append(32)
        test = list.print_list()
        teste = [9, 10, 32]
        self.assertEqual(teste, test)

    def test_insert(self):
        list = Linked_list()
        list.append(9)
        list.append(12)
        list.append(13)
        test = list.insert(2, 89)
        self.assertEqual(test, 89)
    

if __name__ == "__main__":
    unittest.main()