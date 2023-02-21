from src.service.exception import ServiceException


class Ui:

    def __init__(self, service_board):
        self._service_board = service_board

    def print_board(self):
        print(str(self._service_board.get_board()))

    def run(self):
        self.print_board()
        ok = True
        while self._service_board.calculate_left_moves():
            try:
                over =  self._service_board.make_computer_move()
                self.print_board()
                if over == 3:
                    print("Order won...GAME OVER!")
                    exit()
            except ServiceException as se:
                print(se)
            try:
                over = self.make_player_move()
                self.print_board()
                if over == 2:
                    print("Chaos won...CONGRATULATIONS!")
                    exit()
            except ServiceException as se:
                print(se)
        print("Chaos won...CONGRATULATIONS")

    def make_player_move(self):

        print("It's your turn (order) ")

        row = input("Choose row(number between 1 and 6)> ")
        column = input("Choose column(number between 1 and 6)> ")
        element = input("Choose the symbol you want to place (x or o)> ")
        try:
            over = self._service_board.make_player_move(row,column,element)
            return over
        except ServiceException as se:
            print(se)

