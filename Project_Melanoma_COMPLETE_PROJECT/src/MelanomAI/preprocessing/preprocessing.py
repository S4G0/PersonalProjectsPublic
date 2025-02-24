from project_mlds.src.MelanomAI.database import database

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

def function_preprocessing():

  df_train, df_val, df_test =  database.function_database()
  
  ## 2.1. Data Augmentation
  # Definición de función de data augmentation
  
  # Definimos el generador de datos para el conjunto de entrenamiento
  
  train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
      rescale=1./255,
      width_shift_range=0.0,
      height_shift_range=0.0,
      zoom_range=0,
      horizontal_flip=True,
      vertical_flip=True,
      fill_mode= 'constant',
      rotation_range= 45
    )
  
  # Definimos el generador de datos para el conjunto de validación
  val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
  
  # Definimos el generador de datos para el conjunto de prueba
  test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)


  batch_size = 128
  
  train_gen = train_datagen.flow_from_dataframe(
      dataframe=df_train,
      x_col="filename",
      y_col="label",  # Assuming 'label' is the column containing the labels
      target_size=(300,300),
      batch_size=batch_size,
      class_mode="binary",  # It can be categorical
      seed=0
      )
  
  # Set up the generator for validation data
  validation_gen = val_datagen.flow_from_dataframe(
      dataframe=df_val,
      x_col="filename",
      y_col="label",  # Assuming 'label' is the column containing the labels
      target_size=(300,300),
      batch_size=batch_size,
      class_mode="binary",  # It can be categorical
      seed=0
      )
  
  test_gen = test_datagen.flow_from_dataframe(
      dataframe=df_test,
      x_col="filename",
      y_col="label",  # Assuming 'label' is the column containing the labels
      target_size=(300,300),
      batch_size=batch_size,
      class_mode="binary",  # It can be categorical
      seed=0
      )
  
  return train_gen, validation_gen, test_gen, batch_size

