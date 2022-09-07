import math
import os.path
import random
import util
import numpy as np
import urllib.request
from os import path
from typing import IO
from threading import Thread
from lib.preprocessor import get_chessboard_tiles


def generate_n_tilesets(input_dir: str = util.BOARD_DIR, output_dir: str = util.PIECES_DIR) -> None:
    if len(os.listdir(input_dir)) == 0:
        print("No Input Data\nGenerating...")
        generate_n_boards(output_dir=input_dir)

    for file in os.listdir(input_dir):
        sub_dir: str = path.join(output_dir, file.replace(".png", ""))
        img_dir_base: str = path.join(sub_dir, "{}.png")
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
        tiles = get_chessboard_tiles(path.join(input_dir, file))
        if len(tiles) != 64:
            continue
        rows = "abcdefgh"
        cols = "12345678"
        for i in range(8):
            row = rows[i]
            for j in range(8):
                col = cols[j]
                piece = file[i*j]
                img_dir = img_dir_base.format(row + col + "-" + piece)
                print(img_dir)
                tiles[i*j].save(img_dir, format="PNG")


def generate_n_boards(n: int = 1, output_dir: str = util.BOARD_DIR) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(n):
        fen: str = gen_random_fen()
        url: str = jinchess_url_template_generator().format(fen)
        f: IO = open(path.join(output_dir, fen.replace("/", "") + ".png"), 'wb')
        f.write(urllib.request.urlopen(url).read())


def jinchess_url_template_generator() -> str:
    url_template: str = "https://jinchess.com/chessboard/?p={}"
    jinchess_board_themes: [str] = [
        None,
        "cold-marble",
        "gray-tiles",
        "green-marble",
        "pale-wood",
        "red-marble",
        "slate",
        "winter",
        "wooden-dark",
    ]
    jinchess_piece_themes: [str] = [
        None,
        "merida-flat",
        "smart-flat",
        "usual-flat",
        "alpha-flat",
    ]
    theme: str = np.random.choice(jinchess_board_themes)
    pieces: str = np.random.choice(jinchess_piece_themes, 1)[0]
    grayscale: int = math.floor(random.uniform(0, 1))
    if theme is not None:
        url_template += "&bp={}".format(theme)
    if pieces is not None:
        url_template += "&ps={}".format(pieces)
    if grayscale:
        url_template += "&gs"
    return url_template


def gen_random_fen() -> str:
    # fen: str = ""
    # for i in range(64):
    #     fen += pieces[i]
    # return fen
    pieces = np.random.choice(list(util.FEN), 64)
    fen = '/'.join([''.join(pieces[i * 8:(i + 1) * 8]) for i in range(8)])
    return fen


if __name__ == '__main__':
    generate_n_boards(1000)
    generate_n_tilesets()
