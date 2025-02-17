<img src = "https://drive.google.com/uc?export=view&id=1aepHWDYbLzGt5NtGmIAiOiczlaem7_nt" alt = "Encabezado MLDS unidad 2" width = "100%">  </img>

# **0. Installation, charge and import of libraries**

!pip install rlxcrypt

!pip install dvc dvc-gdrive
!pip install mlflow==2.1.0
!apt install tree git

!pip install -U scikit-learn

Importamos las librerías necesarias:

# Librerías de utilidad para manipulación y visualización de datos.
import os
import mlflow
import pandas as pd
import subprocess
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from IPython import get_ipython
from IPython.display import display

# Ignorar warnings.
import warnings
warnings.filterwarnings('ignore')

# Versiones de las librerías usadas.
import sklearn
import dvc
!python --version
print('MLflow', mlflow.__version__)
print('Scikit-learn', sklearn.__version__)
print('DVC', dvc.__version__)

# **1. Inicialización del Repositorio**
---

En este punto debe inicializar un repositorio de `git`. Ejecute la siguiente celda rellenando la información para identificarse:

!git clone https://github.com/S4G0/project_mlds.git

%cd project_mlds/
!ls

!git config --global user.email "sagomezar@unal.edu.co"
!git config --global user.name "S4G0"
#!git config --global init.defaultBranch master

# **2. Data analysis with DVC**

from google.colab import drive
drive.mount('/content/drive')
path="/content/drive/MyDrive/Proyecto Metodologías ágiles para el desarrollo de aplicaciones con ML/Data/"

!pwd

!mkdir data
!ls

!cp -r /content/drive/MyDrive/Proyecto\ Metodologías\ ágiles\ para\ el\ desarrollo\ de\ aplicaciones\ con\ ML/Data/Imágenes/ /content/project_mlds/data

!ls ./data

!git status

!dvc init

!ls -a

!dvc add ./data/Imágenes/

!ls -a ./data/

!git status

!git add ./data/.gitignore data/*.dvc

!git status

!git commit -m "Inicializamos DVC y agregamos el dataset de Melanomas"

!git status

#mlds6-3@mlds6-405100.iam.gserviceaccount.com
drive_id = "14xKJMlBPaIOgNHjV1RkJsqFBxjnPr69L" # reemplace aquí el id de su carpeta
os.environ["DRIVEID"] = drive_id

!dvc remote add -d storage "gdrive://$DRIVEID"

!dvc remote modify storage gdrive_use_service_account true

import json
with open(path+"credentials.json") as f:
    os.environ["GDRIVE_CREDENTIALS_DATA"] = f.read()

!git add .dvc/config
!git commit -m "Agregamos drive remoto a dvc"

#!dvc push

!ls -a

!git push origin master

**Haciendo push a repositorio**

!git remote remove origin

token = "" # Agregue su token dentro de las comillas.

repo_url = "https://github.com/S4G0/project_mlds.git" # Agruegue la url de su repositorio dentro de las comillas.

Ahora, usaremos una expresión regular para reemplazar el token en esta url:

import re
pat = re.compile(r"(https://)(.*)")

Formateamos la URL:

match = re.match(pat, repo_url)
url_token = "".join([match.group(1), token, "@", match.group(2)])
os.environ["GITHUB"] = url_token

!git remote add origin $GITHUB

!git push origin master



Pulling data

!ls data/

!dvc pull

!ls data/

!ls data/Imágenes/
