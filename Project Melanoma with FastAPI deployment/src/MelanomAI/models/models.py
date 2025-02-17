from project_mlds.src.MelanomAI.database import database
from project_mlds.src.MelanomAI.preprocessing import preprocessing

#!pip install dvc dvc-gdrive
#!apt install tree git

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import subprocess
from IPython import get_ipython
from IPython.display import display
#import dvc
from sklearn.model_selection import train_test_split
import tensorflow as tf


def function_model():

  df_train, df_val, df_test =  database.function_database()
  train_gen, validation_gen, test_gen, batch_size =  preprocessing.function_preprocessing()
  
  """## 2.2. Model 1: Red neuronal desde 0
  ### 2.2.1. Definición del modelo"""
  
  def custom_model(units, dropout):
    # Fijamos una semilla para efectos de reproducibilidad
    np.random.seed(0)
    tf.random.set_seed(0)

    # Definimos una arquitectura secuencial para la CNN
    model = tf.keras.Sequential()
    # Capa convolucional con 32 filtros y un kernel 3x3, ativación ReLU
    model.add(tf.keras.layers.Conv2D(32, (4, 4), strides=(2, 2),
    padding="valid", activation='relu', input_shape=(300, 300, 3)))
    # Capa de max pooling
    model.add(tf.keras.layers.AveragePooling2D((2, 2)))
    # Agregamos dropout para regularización
    model.add(tf.keras.layers.Dropout(dropout))
    # Capa convolucional con 64 filtros y un kernel 3x3,activación ReLU
    model.add(tf.keras.layers.Conv2D(64, (4, 4), strides=(2, 2),
    padding="valid", activation='relu'))
    # Capa de max pooling
    model.add(tf.keras.layers.AveragePooling2D((2, 2)))
    # Capa convolucional con 64 filtros y un kernel 3x3,activación ReLU
    model.add(tf.keras.layers.Conv2D(64, (3, 3), strides=(1, 1),
    padding="valid", activation='relu'))
    # Aplana la salida para la capa densa
    model.add(tf.keras.layers.Flatten())
    # Agregamos una capa densa
    model.add(tf.keras.layers.Dense(units, activation='relu'))
    # Agregamos dropout para regularización
    model.add(tf.keras.layers.Dropout(dropout))
    # agrega una capa de salida
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    return model
    
  dropout=0.2
  neurons_in_dense_layer=32
  model_test = custom_model(units=neurons_in_dense_layer, dropout=dropout)
  model_test.summary()
  
  """### 2.2.2. Compilar el modelo"""
  def compile_model(model, l_r, metrics):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    # Compilamos el modelo
    model.compile(loss='binary_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=l_r),
                  metrics=metrics)
    return model
  
  learning_rate=1e-3
  test_model = compile_model(
                          model=model_test,
                          l_r=learning_rate,
                          metrics=['accuracy']
                           )
  test_model.get_compile_config()

  return test_model, dropout, neurons_in_dense_layer, learning_rate
