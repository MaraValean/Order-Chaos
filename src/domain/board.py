from texttable import Texttable


class Board:
    def __init__(self):
        self.__board = [[" " for i in range(6)] for j in range(6)]

    def validate_placement(self, row, column, element):
        """

        :param row:
        :param column:
        :return:
        """
        if self.__board[row][column] == element:
            return False
        #row_coords = [-1, -1, 0, 1, 1, 1, 0, -1]
        row_coords = [-1,-1,-1,0,0,1,1,1]
        #column_coords = [0, 1, 1, 1, 0, -1, -1, -1]
        column_coords = [-1,0,1,-1,1,-1,0,1]
        for i in range(6):
            x = row + row_coords[i]
            y = column + column_coords[i]
            if x >= 0 and y >= 0 and x < 8 and y < 8 and self.__board[x][y] == element:
                return False
        return True

    def get_board_element(self,row,column):
        return self.__board[row][column]

    def set_board_element(self, row, column, element):
        board = self.__board
        board[row][column] = element

    def get_board(self):
        return self.__board

    def find_element(self,element):
        board = self.__board
        for row in range(0,6):
            for column in range(0,6):
                if board[row][column] == element:
                    return (row,column)
        return (-1,-1)

    def __str__(self):
        """
        Convert the box in a string format, used for printing in the UI
        :return:
        """
        table = Texttable()
        table.add_row([0, 1, 2, 3, 4, 5, 6])
        character = "123456"
        for row in range(6):
            row_to_add = [character[row]]
            for column in range(6):
                """
                if self.__board[row][column] == 'B':
                    if self.validate_placement(row, column,'E'):
                        row_to_add.append(' ')
                    else:
                        row_to_add.append('B')
                else:
                """
                row_to_add.append(self.__board[row][column])
            table.add_row(row_to_add)
        return table.draw()

    def verify_valid_move(self, row, column):
        if 5 >= row >= 0 and 5 >= column >= 0 and self.__board[row][column] == ' ':
                return True
        return False
