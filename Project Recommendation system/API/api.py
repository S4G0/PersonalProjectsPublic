from fastapi import FastAPI, HTTPException, Query
import joblib
import pandas as pd
from pydantic import BaseModel
import os
from modelo import *

# Specify the folder you want to search
df_users = pd.read_csv("data/users_tr.csv")
df_products = pd.read_csv("data/products_tr.csv")
df_interactions = pd.read_csv("data/interactions_tr.csv")

# Crear una instancia de FastAPI
app = FastAPI()

# Ruta de prueba
@app.get("/recommendations")
def read_item(user_id: int):
	if not((user_id>=1)&(user_id<=5000)&(user_id in df_interactions['user_id'].values)):
	        raise HTTPException(status_code=400, detail="El usuario no se encuentra en la base de datos para realizar una recomendación personalizada.")
	return str(generate_recommendations(df_interactions,df_products,df_users,user_id))

