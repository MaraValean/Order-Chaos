# Order-Chaos
code written at the Fundamentals of Programming exam

Order and chaos is a pen and pencil strategy game played on a 6x6 board. The two players are order (computer player) and chaos (human player), and they take turns placing X's and O's on the board Order wins by having consecutive pieces of the same type in a row, column or a diagonal. Chaos wins when the board is filed without this happening. Unlike other games, players can pick which symbol to place every move. Implement a console-based program that allows a human to thwart the computer's efforts. The program must work as follows

1. When the program is started, the empty board is displayed (1p).
2. Players take turn in placing symbols on the board, with order having the first move (1p)
3. User input is validated and an error message shown when trying to make an illegal move. [1p)
4. In order to win, the computer uses the following strategy:
  a. Always makes valid moves [1p).
  b. If it can make a winning move, it does [1.5p).
  c. Chooses the symbol that appears most often on the board (1p), and places it in the square that has the largest number of same-symbol neighbours (1p).
  
5. If there are 5 consecutive symbols of the same type in a row, column or diagonal order wins and the game is finished (1p). (NB! This can also happen after chaos moves)
6. If the board is full, chaos wins and the game is finished (0.5p).
