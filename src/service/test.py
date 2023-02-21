import unittest

from src.domain.board import Board
from src.service.service import Service


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.__service = Service(Board())

    def test_check_winning_move(self):
        pass
