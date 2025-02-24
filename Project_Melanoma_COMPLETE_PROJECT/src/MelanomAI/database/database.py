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

# Ignorar warnings.
import warnings
warnings.filterwarnings('ignore')


def function_database():
  

  # Commented out IPython magic to ensure Python compatibility.
  #!git clone https://github.com/S4G0/project_mlds.git
  # %cd project_mlds/
  #!ls
  #!git config --global user.email "sagomezar@unal.edu.co"
  #!git config --global user.name "S4G0"

  from google.colab import drive
  drive.mount('/content/drive')
  path="/content/drive/MyDrive/Proyecto Metodologías ágiles para el desarrollo de aplicaciones con ML/Data/"

  #ID del drive donde están los datos versionados
  drive_id = "14xKJMlBPaIOgNHjV1RkJsqFBxjnPr69L" # reemplace aquí el id de su carpeta
  os.environ["DRIVEID"] = drive_id

  #Se importa el archivo credentials.json del repositorio
  import json
  with open("credentials.json") as f:
    os.environ["GDRIVE_CREDENTIALS_DATA"] = f.read()
    
  # Se traen los datos
  #!dvc pull

  list_name_original_benign=[]
  list_name_original_malignant=[]
  list_name_test_benign=[]
  list_name_test_malignant=[]

  for dirname, _, filenames in os.walk('./data/Imágenes/train/malignant'):
      for filename in filenames:
          list_name_original_malignant.append(os.path.join(dirname, filename))

  for dirname, _, filenames in os.walk('./data/Imágenes/train/benign'):
      for filename in filenames:
         list_name_original_benign.append(os.path.join(dirname, filename))

  for dirname, _, filenames in os.walk('./data/Imágenes/test/malignant'):
      for filename in filenames:
          list_name_test_malignant.append(os.path.join(dirname, filename))

  for dirname, _, filenames in os.walk('./data/Imágenes/test/benign'):
      for filename in filenames:
          list_name_test_benign.append(os.path.join(dirname, filename))

  df_original_benign = pd.DataFrame({'filename': list_name_original_benign})
  df_original_benign['label'] = "0"

  df_test_benign = pd.DataFrame({'filename': list_name_test_benign})
  df_test_benign['label'] = "0"

  #--------------------------------------------------------------------
  df_original_malignant = pd.DataFrame({'filename': list_name_original_malignant})
  df_original_malignant['label'] = "1"

  df_test_malignant = pd.DataFrame({'filename': list_name_test_malignant})
  df_test_malignant['label'] = "1"

  df_train_benign, df_validation_benign = train_test_split(df_original_benign, test_size=0.2, random_state=0)
  df_train_malignant, df_validation_malignant = train_test_split(df_original_malignant, test_size=0.2, random_state=0)

  df_train = pd.concat([df_train_benign,      df_train_malignant])
  df_val   = pd.concat([df_validation_benign, df_validation_malignant])
  df_test  = pd.concat([df_test_benign,       df_test_malignant])

  return df_train, df_val, df_test

