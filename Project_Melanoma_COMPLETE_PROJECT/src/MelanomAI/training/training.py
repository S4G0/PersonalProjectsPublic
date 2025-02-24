from project_mlds.src.MelanomAI.database import database
from project_mlds.src.MelanomAI.preprocessing import preprocessing
from project_mlds.src.MelanomAI.models import models 

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


def function_training():
  
  train_gen, validation_gen, test_gen, batch_size =  preprocessing.function_preprocessing()
  test_model, dropout, neurons_in_dense_layer, learning_rate = models.function_model()
  
  """## 2.2.3. Entrenar el modelo"""
  def train_model(model, train_gen, val_gen, epochs, weights):
    # Fijamos una semilla para efectos de reproducibilidad
    np.random.seed(0)
    tf.random.set_seed(0)  # Usar tf.random.set_seed en lugar de tf.keras.utils.set_random_seed

    # Calcular el número de imágenes en los conjuntos de entrenamiento y validación
    num_train_images = 7684
    num_val_images = 1921

    # Definir el callback para guardar el mejor modelo
    best_callback = tf.keras.callbacks.ModelCheckpoint(filepath=weights,
                                                       monitor='val_loss',
                                                       verbose=1,
                                                       save_best_only=True,
                                                       save_weights_only=True,
                                                       mode='min')
    # Entrenar el modelo
    history = model.fit(train_gen,
                        steps_per_epoch=num_train_images//batch_size,
                        validation_data=val_gen,
                        validation_steps=num_val_images//batch_size,
                        epochs=epochs,
                        callbacks=[best_callback])

    return model, history
  
  #Entrenamiento del modelo
  epochs=30
  model_tr, history = train_model(model=test_model,
                                train_gen=train_gen,
                                val_gen=validation_gen,
                                epochs=epochs,
                                weights='weights.h5')
  
  #Información
  print(history.history.keys())
  print('El modelo se ha entrenado durante',len(history.history['val_accuracy']),'epochs')
  if os.path.isfile('weights.h5'):
    print("Los pesos se guardaron en 'weights.h5'")
  
  return model_tr, history, epochs, weights
