import unittest
import ListCompare


class TestListCompare(unittest.TestCase):
    def test_compare_lists(self):
        lc = ListCompare.ListCompare([4,4,4],[5,5,5])
        self.assertEquals(lc.compare_lists(), "Второй список имеет большее среднее значение")

        lc = ListCompare([9, 7, 8], [4, 5, 6])
        self.assertEquals(lc.compare_lists, "Первый список имеет большее среднее значение")

        lc = ListCompare([1, 2, 3], [1, 2, 3])
        self.assertEquals(lc.compare_lists, "Средние значения равны")


if __name__ == '__main__':
    unittest.main()
