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
            match row:
                case 1:
                    return [
                        Square.at(row+1, col), 
                        Square.at(row+2, col)
                        ]
                case 7:
                    return []
                case _:
                    return [Square.at(row+1, col)]
                    
        elif colour == Player.BLACK:
            match row:
                case 0:
                    return []
                case 6:
                    return [
                        Square.at(row-1, col), 
                        Square.at(row-2, col)
                        ]
                case _:
                    return [Square.at(row-1, col)]


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