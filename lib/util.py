import re

# Digits in FEN notation (capital = white, lowercase = black)
FEN: str = "1RNBQKPrnbqkp"
BOARD_DIR: str = "./images_board"
PIECES_DIR: str = "./images_pieces"
MODELS_DIR: str = "../models"


def simplify_fen(complicated_fen: str) -> str:
    for length in reversed(range(2, 9)):
        complicated_fen = complicated_fen.replace(length * '1', str(length))
    return complicated_fen


def complicate_fen(simplified_fen: str) -> str:
    for digit in re.findall(r'[2-8]', simplified_fen):
        simplified_fen = simplified_fen.replace(digit, int(digit) * '1')
    return simplified_fen
