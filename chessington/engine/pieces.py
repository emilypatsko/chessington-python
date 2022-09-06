from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        colour = self.player
        current_square = board.find_piece(self)
        row, col = current_square.row, current_square.col
   
        if colour == Player.WHITE:
            square_2 = Square.at(row+2,col)
            square_1 = Square.at(row+1,col)
            
            match row:
                case 1: 
                    out = []
                    if board.get_piece(square_1) == None:
                        out.append(square_1)
                        if board.get_piece(square_2) == None:
                            out.append(square_2)
                    return out
                case 7:
                    return []
                case _:
                    if board.get_piece(Square.at(row+1, col)) == None:
                        return [Square.at(row+1, col)]
                    else:
                        return []
                    
        elif colour == Player.BLACK:
            
            handle_move(row-1, row-2, col, board, row, self.player)


def handle_move(row_ahead_1, row_ahead_2, column, board: Board, row: int, player):

    end_of_board, starting_row = 0, 6 if player==Player.BLACK else 7, 1
    
    square_one_in_front = Square.at(row_ahead_1, column)
    square_two_in_front = Square.at(row_ahead_2, column)

    one_in_front_free = board.get_piece(square_one_in_front) == None
    two_in_front_free = board.get_piece(square_two_in_front) == None    

    match row:
        case end_of_board:
            return []
        case starting_row:
            out = []
            if one_in_front_free:
                out.append(square_one_in_front)

                if two_in_front_free:
                    out.append(square_two_in_front)
            return out
        case _:
            if one_in_front_free:
                return [square_one_in_front]
            else:
                return []

    

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []