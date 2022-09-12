import util
import numpy as np
import tensorflow as tf
from glob import glob
from keras import models, layers


def load_tiles(tiles):
    images = []
    labels = []
    for tile in tiles:
        piece = tile[-5]
        if not piece in util.FEN:
            continue
        images.append(np.array
                      (tf.image.resize
                       ((tf.image.convert_image_dtype
                         (tf.image.decode_image
                          (tf.io.read_file(tile), channels=1), tf.float32)), [32, 32])))
        labels.append(util.FEN.index(piece))
        print(tile + " " + piece + " " + str(labels))
    images = np.array(images)
    labels = np.array(labels)
    return [images, labels]


if __name__ == '__main__':
    all_tiles = np.array(glob("{}/*/*".format(util.PIECES_DIR)))
    np.random.shuffle(all_tiles)
    divider = int(len(all_tiles) * 0.85)
    train_tiles = all_tiles[:divider]
    test_tiles = all_tiles[divider:]

    train_images, train_labels = load_tiles(train_tiles)
    test_images, test_labels = load_tiles(test_tiles)

    input_shape = (32, 32, 1)
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(len(util.FEN), activation='softmax'),
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=20, validation_data=(test_images, test_labels))
    models.save_model(model, util.MODELS_DIR, overwrite=True)
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
