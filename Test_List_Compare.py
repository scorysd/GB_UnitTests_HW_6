import unittest
import List_Compare


class TestListCompare(unittest.TestCase):
    def test_compare_lists(self):
        list_compare = List_Compare.ListCompare([2, 3, 4], [4, 5, 6])
        self.assertEqual(list_compare.compare_lists(), -1)

        list_compare = List_Compare.ListCompare([9, 9, 9], [4, 5, 6])
        self.assertEqual(list_compare.compare_lists(), 1)

        list_compare = List_Compare.ListCompare([2, 3, 4], [2, 3, 4])
        self.assertEquals(list_compare.compare_lists(), 0)

if __name__ == '__main__':
    unittest.main()
