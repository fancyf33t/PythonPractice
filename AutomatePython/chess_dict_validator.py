# Write a function nammed isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can't be on space '9z'.
# The pieces will begin with either a 'w' or 'b' to represent black or white, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

white_pieces = {
    'wking': 1,
    'wqueen': 1,
    'wbishop': 2,
    'wknight': 2,
    'wrook': 2,
    'wpawn': 8
}
black_pieces = {
    'bking': 1,
    'bqueen': 1,
    'bbishop': 2,
    'bknight': 2,
    'brook': 2,
    'bpawn': 8
}
