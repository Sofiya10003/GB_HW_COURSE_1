class Matrix:
    def __init__(self,list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        my_line = ''
        for i in self.list_of_lists:
            my_line += str(i) + '\n'
        return my_line

    def __add__(self, other):
        new_list_sum = []
        new_line = ''
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                new_list_sum.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            new_line = new_line + str(new_list_sum)+'\n'
            new_list_sum = []
        return new_line


a_matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
b_matrix = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print(a_matrix)
print(b_matrix)

print(a_matrix + b_matrix)