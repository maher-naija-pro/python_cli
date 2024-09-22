#!/usr/bin/python
import neurodeploy as neuro
import os

import tensorflow as tf
from tensorflow import keras


# Define a simple sequential model
def create_model():
    model = tf.keras.models.Sequential(
        [
            keras.layers.Dense(512, activation="relu", input_shape=(784,)),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10),
        ]
    )

    model.compile(
        optimizer="adam",
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[tf.metrics.SparseCategoricalAccuracy()],
    )

    return model


# Create a basic model instance
model = create_model()

neuro.deploy("ffff", model)
