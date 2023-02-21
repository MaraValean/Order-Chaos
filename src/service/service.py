from src.service.exception import ServiceException


class Service:

    def __init__(self, board):

        self._board = board

    def get_board_string(self):
        board = self._board.get_board_string()
        return board

    def make_move(self, row, column, symbol):
        if self._board.verify_valid_move(row, column):
            self._board.set_board_element(row,column, symbol)
        else:
            raise ServiceException

    def calculate_number_of_elements(self, row, column,element):
        number_of_elements = 0
        board = self._board.get_board()
        if 0 <= row - 1 <= 5 and 0 <= column - 1 <= 5 and board[row - 1][column - 1] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row - 1 <= 5 and 0 <= column <= 5 and board[row - 1][column] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row - 1 <= 5 and 0 <= column + 1 <= 5 and board[row - 1][column + 1] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row + 1 <= 5 and 0 <= column - 1 <= 5 and board[row + 1][column - 1] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row + 1 <= 5 and 0 <= column <= 5 and board[row + 1][column] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row + 1 <= 5 and 0 <= column + 1 <= 5 and board[row + 1][column + 1] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row <= 5 and 0 <= column + 1 <= 5 and board[row][column + 1] == element:
            number_of_elements = number_of_elements + 1
        if 0 <= row <= 5 and 0 <= column - 1 <= 5 and board[row][column - 1] == element:
            number_of_elements = number_of_elements + 1
        return number_of_elements

    def calculate_best_move(self,element):
        best_row = 0
        best_column = 0
        maximum_elements = -1
        for row in range(0, 6):
            for column in range(0, 6):
                if self._board.verify_valid_move(row, column):
                    move = self.calculate_number_of_elements(row, column,element)
                    if move > maximum_elements:
                        maximum_elements = move
                        best_row = row
                        best_column = column
        return (best_row, best_column)

    def calculate_left_moves(self):
        for row in range(0, 6):
            for column in range(0, 6):
                if self._board.verify_valid_move(row, column):
                    return True
        return False

    def get_board(self):
        """
        Return the game board
        :return:
        """
        return self._board

    def make_computer_move(self):
        """
        This function chooses a move for the computer by searching for a winning move, or putting the symbol which appears most often and placing it in the square with largest number of same-symbol neighbours
       :return: 3 if the move is a winning one, 1 otherwise
       """
        nr_x = nr_o = 0
        """
        for row in range(0, 6):
            for column in range(0, 6):
                if self.check_winning_move(row,column,"x"):
                    self.make_move(row,column,"x")
                    return 3
                if self.check_winning_move(row, column, "o"):
                    self.make_move(row, column, "o")
                    return 3
        """
        for row in range(0,6):
            for column in range(0,6):
                if self._board.get_board_element(row,column) == "x":
                    nr_x += 1
                elif self._board.get_board_element(row,column) == "o":
                    nr_o +=1
        if nr_x >= nr_o:
            element = "x"
        else:
            element = "o"
        row,column = self.calculate_best_move(element)
        """
        max_elem = best_row = best_column = -1
        for row in range(0,6):
            for column in range(0,6):
                nr_elem = self.calculate_number_of_elements(row,column,element)
                if nr_elem > max_elem:
                    max_elem = nr_elem
                    best_row = row
                    best_column = column
        self.make_move(row,column,element)
        #self.make_move(best_row,best_column,element)
        #row = best_row
        #column = best_column
        """
        self.make_move(row,column,element)
        if self.check_winning_move(int(row) - 1, int(column) - 1, element):
            return 3
        return 1

    def make_player_move(self,row,column,element):
        """
        This is the function that makes the move chosen by the player, if it is valid
        :param row: an integer number representing the coordinate of the row of the element on which the move is made
        :param column: an integer number representing the coordinate of the column of the element on which the move is made
        :param element: the symbol we place with the move, either "x' ore "o"
        :return: 2 if the move is a winning one, 1 otherwise
        :raises ServiceException if move is not valid
        """
        if not row.isnumeric():
            raise ServiceException("Row must be an integer")
        elif int(row) <1 or int(row) >6:
            raise ServiceException("Row must be an integer between 1 and 6")
        if not column.isnumeric():
            raise ServiceException("Column must be an integer")
        elif int(column)<1 or int(column) >6:
            raise ServiceException("column must be an integer between 1 and 6")
        if element != "x" and element != "o":
            raise ServiceException("Symbol must be x or o")
        if self._board.verify_valid_move(int(row)-1, int(column)-1):
            self.make_move(int(row)-1,int(column)-1,element)
            if self.check_winning_move(int(row)-1,int(column)-1,element):
                return 2
        else:
            raise ServiceException("invalid move")
        return 1

    def check_winning_move(self,row,column,element):
        """
        This is the function that checks if a certain move is a winning one by calculating if we have 5 same-symbol cells either on the same diagonal,same row or same column
        :param row: an integer number representing the coordinate of the row of the element on which the move is made
        :param column: an integer number representing the coordinate of the column of the element on which the move is made
        :param element: the symbol we place with the move, either "x' ore "o"
        :return: True if the move is a winning one, Fale otherwise
        """
        nr_el = 0
        for i in range(6):
            if self._board.get_board_element(row, i) == element:
                nr_el += 1
        if nr_el >= 5:
            return True
        nr_el = 0
        for i in range(6):
            if self._board.get_board_element(i, column) == element:
                nr_el += 1
        if nr_el >= 5:
            return True
        nr_el = 0
        for i in range(6):
            for j in range(6):
                if i-j == row - column:
                    if self._board.get_board_element(i,j) == element:
                        nr_el += 1
        if nr_el >= 5:
            return True
        nr_el = 0
        for i in range(6):
            for j in range(6):
                if i + j == row + column:
                    if self._board.get_board_element(i,j) == element:
                        nr_el += 1
        if nr_el >= 5:
            return True
        return False

    def calculate_elements_computer_move(self,row,column,element):
        nr_el = 0
        for i in range(6):
            if self._board.get_board_element(row, i) == element:
                nr_el += 1
        for i in range(6):
            if self._board.get_board_element(i, column) == element:
                nr_el += 1

        for i in range(6):
            for j in range(6):
                if i - j == row - column:
                    if self._board.get_board_element(i, j) == element:
                        nr_el += 1

        for i in range(6):
            for j in range(6):
                if i + j == row + column:
                    if self._board.get_board_element(i, j) == element:
                        nr_el += 1
        return nr_el
