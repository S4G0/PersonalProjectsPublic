# -*- coding: utf-8 -*-
"""evaluation_and_MLFlow_registration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/185Cd7fFBDWa3P7GH2xoEn0cjyJmf-fOt
"""

!apt install tree git
!pip install pyngrok
!pip install mlflow==2.1.0

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import subprocess
from IPython import get_ipython
from IPython.display import display
from sklearn.model_selection import train_test_split
import tensorflow as tf
import mlflow

# Ignorar warnings.
import warnings
warnings.filterwarnings('ignore')

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/S4G0/project_mlds.git
# %cd project_mlds/
!ls
!git config --global user.email "sagomezar@unal.edu.co"
!git config --global user.name "S4G0"

"""##**0. DATA**"""

from google.colab import drive
drive.mount('/content/drive')
path="/content/drive/MyDrive/Proyecto Metodologías ágiles para el desarrollo de aplicaciones con ML/Data/"

list_name_test_benign=[]
list_name_test_malignant=[]

for dirname, _, filenames in os.walk(path+'Imágenes/test/malignant'):
    for filename in filenames:
        list_name_test_malignant.append(os.path.join(dirname, filename))

for dirname, _, filenames in os.walk(path+'Imágenes/test/benign'):
    for filename in filenames:
        list_name_test_benign.append(os.path.join(dirname, filename))

df_test_benign = pd.DataFrame({'filename': list_name_test_benign})
df_test_benign['label'] = "0"

df_test_malignant = pd.DataFrame({'filename': list_name_test_malignant})
df_test_malignant['label'] = "1"

df_test  = pd.concat([df_test_benign,       df_test_malignant])

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

test_gen = test_datagen.flow_from_dataframe(
    dataframe=df_test,
    x_col="filename",
    y_col="label",  # Assuming 'label' is the column containing the labels
    target_size=(300,300),
    batch_size=128,
    class_mode="binary",  # It can be categorical
    seed=0
)

"""# **1. Selección y diseño de modelos**
---

### 1.1. Definición del modelo
"""

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
learning_rate=1e-3
epochs=30

model_test = custom_model(units=neurons_in_dense_layer, dropout=dropout)
model_test.summary()

"""### 1.2. Compilar el modelo"""

def compile_model(model, l_r, metrics):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    # Compilamos el modelo
    model.compile(loss='binary_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=l_r),
                  metrics=metrics)

    return model

test_model = compile_model(
                          model=model_test,
                          l_r=learning_rate,
                          metrics=['accuracy']
                           )
test_model.get_compile_config()

"""## 1.3. Cargar modelo"""

!ls data

test_model.load_weights('./data/weights.h5')

"""## 1.4. Evaluar el modelo"""

def evaluate_model(model, test_gen):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    metrics = model.evaluate(test_gen)
    return metrics

# Evaluación del modelo
metrics = evaluate_model(test_model, test_gen)

# Resultados de la evaluación
print("Resultados de la evaluación:")
print("Loss:", metrics[0])
print("Accuracy:", metrics[1])
print(f"En este caso el {metrics[1]*100:.2f}% de las muestras fueron clasificadas correctamente por el modelo.")

"""## 1.5. MLFlow - Deployment"""

# Commented out IPython magic to ensure Python compatibility.
!ls scripts
# %cd scripts

# Commented out IPython magic to ensure Python compatibility.
!mkdir evaluation_and_deployment
# %cd evaluation_and_deployment

command = """
mlflow server \
        --backend-store-uri sqlite:///tracking.db \
        --default-artifact-root file:mlruns \
        -p 5000 &
"""
get_ipython().system_raw(command)

"""Ahora debe agregar su token de `ngrok`:"""

token = "2Y3EvQj4U0dEbOuzgzpllybfnub_248exjXrHv2FsqRTozFmG" # Agregue el token dentro de las comillas
os.environ["NGROK_TOKEN"] = token

"""Nos autenticamos en ngrok:"""

!ngrok authtoken $NGROK_TOKEN

"""Ahora, lanzamos la conexión con ngrok:"""

from pyngrok import ngrok
ngrok.connect(5000, "http")

"""Especificamos que MLFlow debe usar el servidor que estamos manejando."""

mlflow.set_tracking_uri("http://localhost:5000")

"""Creamos un experimento:"""

exp = mlflow.create_experiment(name="Melanoma_analysis", artifact_location="mlruns")

run = mlflow.start_run(experiment_id = exp, run_name="Melanoma_model_v0.0.1")
mlflow.sklearn.log_model(test_model, "model")
mlflow.log_params({"dropout": dropout, "neurons_in_dense_layer": neurons_in_dense_layer, "learning_rate": learning_rate, "epochs": epochs})
mlflow.log_metrics({"Loss": metrics[0], "Accuracy": metrics[1]})
mlflow.log_artifact("../../data/weights.h5", "weights")
mlflow.end_run()

!ls

!git status

!git add ../evaluation_and_deployment/

!git status

!git commit -m "All MLFlow files are added"

!git status

"""**Haciendo push a repositorio**"""

!git remote remove origin

token = "" # Agregue su token dentro de las comillas.
repo_url = "https://github.com/S4G0/project_mlds.git" # Agruegue la url de su repositorio dentro de las comillas.

#Ahora, usaremos una expresión regular para reemplazar el token en esta url:
import re
pat = re.compile(r"(https://)(.*)")

#Formateamos la URL:
match = re.match(pat, repo_url)
url_token = "".join([match.group(1), token, "@", match.group(2)])
os.environ["GITHUB"] = url_token

!git remote add origin $GITHUB

!git push origin master

#model=mlflow.pyfunc.load_model("models:/Melanoma/Production")
