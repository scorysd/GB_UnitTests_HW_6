class ListCompare:
    def __int__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    @staticmethod
    def calculate_average(num_list):
        if len(num_list) > 0:
            return sum(num_list) / len(num_list)
        else:
            return 0

    def compare_lists(self):
        avg_1 = self.calculate_average(self.list1)
        avg_2 = self.calculate_average(self.list2)
        if avg_1 > avg_2:
            print("Первый список имеет большее среднее значение")
        elif avg_2 > avg_1:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
