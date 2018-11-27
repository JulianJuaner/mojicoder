from __future__ import absolute_import

from keras.layers import Input, Dense, Dropout, \
                         RepeatVector, LSTM, concatenate, \
                         Conv2D, MaxPooling2D, Flatten, BatchNormalization
from keras.models import Sequential, Model
from keras.optimizers import RMSprop, Adam, SGD
import numpy as np
from keras import *
from Config import *
from CNNModel import *


class EmoPred(CNNModel):
    def __init__(self, input_shape, output_size, output_path):
        CNNModel.__init__(self, input_shape, output_size, output_path)
        self.name = "emotion_prediction_contract"

        image_model = Sequential()
        image_model.add(Conv2D(32, (3, 3), padding='valid', activation='relu', input_shape=input_shape))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Conv2D(32, (3, 3), padding='valid', activation='relu'))
        image_model.add(MaxPooling2D(pool_size=(2, 2)))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Dropout(0.2))

        image_model.add(Conv2D(64, (3, 3), padding='valid', activation='relu'))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Conv2D(64, (3, 3), padding='valid', activation='relu'))
        image_model.add(MaxPooling2D(pool_size=(2, 2)))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Dropout(0.2))

        image_model.add(Conv2D(128, (3, 3), padding='valid', activation='relu'))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Conv2D(128, (3, 3), padding='valid', activation='relu'))
        image_model.add(MaxPooling2D(pool_size=(2, 2)))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Dropout(0.2))

        image_model.add(Flatten())
        image_model.add(Dense(2048, activation='relu'))
        image_model.add(BatchNormalization(momentum = 0.95))
        image_model.add(Dropout(0.5))
        image_model.add(Dense(output_size, activation='softmax'))

        visual_input = Input(shape=input_shape)
        encoded_label = image_model(visual_input)

        self.model = Model(inputs=[visual_input], outputs=encoded_label)
        optimizer = Adam(lr = 1e-4)
        self.model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics = ['mae', 'acc'])

    #without consideration of memory intensive, just fit().
    def fit(self, x, y):
        self.model.fit(verbose = 1, x = x, y = y, shuffle = True, epochs = 1, batch_size = 256)
        self.save()

    def predict(self, image):
        return self.model.predict(image, verbose=0)

    def pred_accuracy(self, test_image, target):
        score = self.model.evaluate(test_image, target)
        print(score)
        return score

    def predict_batch(self, images):
        return self.model.predict(images, verbose=1)
