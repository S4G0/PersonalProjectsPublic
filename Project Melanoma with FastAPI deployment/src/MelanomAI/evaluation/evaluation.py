from project_mlds.src.MelanomAI.database import database
from project_mlds.src.MelanomAI.preprocessing import preprocessing
from project_mlds.src.MelanomAI.models import models 
from project_mlds.src.MelanomAI.training import training

#!pip install dvc dvc-gdrive
#!apt install tree git
#!pip install mlflow==2.1.0
#!pip install pyngrok


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
import mlflow


# Commented out IPython magic to ensure Python compatibility.
#!mkdir evaluation_and_deployment
# %cd evaluation_and_deployment

#command = """
#mlflow server \
#        --backend-store-uri sqlite:///tracking.db \
#        --default-artifact-root file:mlruns \
#        -p 5000 &
#"""
#
#get_ipython().system_raw(command)

#"""Ahora debe agregar su token de `ngrok`:"""

#token = "2Y3EvQj4U0dEbOuzgzpllybfnub_248exjXrHv2FsqRTozFmG" # Agregue el token dentro de las comillas
#os.environ["NGROK_TOKEN"] = token

#"""Nos autenticamos en ngrok:"""

#!ngrok authtoken $NGROK_TOKEN

#"""Ahora, lanzamos la conexión con ngrok:"""

#from pyngrok import ngrok
#ngrok.connect(5000, "http")

#"""Especificamos que MLFlow debe usar el servidor que estamos manejando."""

#mlflow.set_tracking_uri("http://localhost:5000")

#"""Creamos un experimento:"""

#exp = mlflow.create_experiment(name="Melanoma_analysis", artifact_location="mlruns")

#para ejecutar la siguiente función, se debe crear un experimento en mlflow previamente.

def function_evaluation(exp):

  train_gen, validation_gen, test_gen, batch_size =  preprocessing.function_preprocessing()
  model, dropout, neurons_in_dense_layer, learning_rate = models.function_model()
  test_model, history, epochs, weights = training.function_training()

  def evaluate_model(model, test_gen):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    metrics = model.evaluate(test_gen)
    return metrics

  # Evaluación del modelo
  metrics = evaluate_model(test_model, test_gen)
  loss = metrics[0]
  accuracy = metrics[1]
  # Resultados de la evaluación

  print("Resultados de la evaluación:")
  print("Loss:", metrics[0])
  print("Accuracy:", metrics[1])
  print(f"En este caso el {metrics[1]*100:.2f}% de las muestras fueron clasificadas correctamente por el modelo.")
        

  run = mlflow.start_run(experiment_id = exp, run_name="Melanoma_model_v0.0.1")
  mlflow.sklearn.log_model(test_model, "model")
  mlflow.log_params({"dropout": dropout, "neurons_in_dense_layer": neurons_in_dense_layer, "learning_rate": learning_rate, "epochs": epochs})
  mlflow.log_metrics({"Loss": metrics[0], "Accuracy": metrics[1]})
  mlflow.log_artifact("../../data/weights.h5", "weights")
  mlflow.end_run()

  
  return loss, accuracy, weights
  
