from src.domain.board import Board
from src.service.service import Service
from src.ui.ui import Ui

board = Board()
serv = Service(board)
ui = Ui(serv)
ui.run()