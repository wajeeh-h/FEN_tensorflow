import numpy as np
import PIL.Image


def _get_resized_chessboard(chessboard_img_path) -> PIL.Image:
    try:
        img_data = PIL.Image.open(chessboard_img_path).convert('RGB')
    except PIL.UnidentifiedImageError:
        return None
    return img_data.resize([256, 256], PIL.Image.Resampling(2))


def get_chessboard_tiles(chessboard_img_path, use_grayscale=True) -> list[PIL.Image]:
    img_data = _get_resized_chessboard(chessboard_img_path)
    if img_data is None:
        return []
    if use_grayscale:
        img_data = img_data.convert('L', (0.2989, 0.5870, 0.1140, 0))
    chessboard_256x256_img = np.asarray(img_data, dtype=np.uint8)
    tiles = [None] * 64
    for row in range(8):
        for col in range(8):
            sq_i = row * 8 + col
            tile = np.zeros([32, 32, 3], dtype=np.uint8)
            for i in range(32):
                for j in range(32):
                    if use_grayscale:
                        tile[i, j] = chessboard_256x256_img[
                            row * 32 + i,
                            col * 32 + j,
                        ]
                    else:
                        tile[i, j] = chessboard_256x256_img[
                                     row * 32 + i,
                                     col * 32 + j,
                                     :,
                                     ]
            tiles[sq_i] = PIL.Image.fromarray(tile, 'RGB')
    return tiles
