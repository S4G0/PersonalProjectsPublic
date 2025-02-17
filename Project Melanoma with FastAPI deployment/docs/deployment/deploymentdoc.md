# Despliegue de modelos

## Infraestructura

**1. Nombre del modelo:** weights.h5 (este contiene el modelo, no los pesos).

**2. Plataforma de despliegue:** La plataforma donde se va a desplegar el modelo es FastApi.

**3. Requisitos técnicos:** Los requisitos técnicos necesarios para el despliegue son:
  fastapi
  pydantic
  tensorflow>=2.10.0 (versión usada 2.14.0)  
  pillow
  uvicorn
  La versión de Python usada para desarrollar el modelo fue 3.10.12.
  
**4. Requisitos de seguridad:** El modelo desarrollado no tiene requisitos de seguridad necesarios para el despliegue.
 
**5. Diagrama de arquitectura:**

Cliente -> Consulta (Imagen a analizar)-> FastApi y script de despliegue (ver punto 10 de este documento) -> Railway -> Repositorio -> Modelo (ejecución) -> Respuesta (Clasificación del melanoma 1=Maligno yo 0=Benigno) -> Cliente


## Código de despliegue
**6. Archivo principal:** Main.py
  
**7. Rutas de acceso a los archivos:** Los archivos necesarios para el despliegue están disponibles en: https://github.com/S4G0/project_mlds/tree/master/scripts/evaluation_and_deployment
  
## Documentación del despliegue

**8. Instrucciones de instalación:** A continuación las instrucciones detalladas para instalar el modelo en la plataforma de despliegue:
- Clonar el Repositorio: Clonar el repositorio que contiene el código del modelo desde el repositorio remoto "git clone https://github.com/S4G0/project_mlds.git".
- Instalar dependencias: Disponibles en el primer punto de infraestructura de este archivo (requisitos técnicos).
  
**9. Instrucciones de configuración:**-
- Instalar las siguientes librerías¨:
  from PIL import Image
  from pydantic import BaseModel
  from typing import List
  import requests
  import numpy as np
  import os


**10. Instrucciones de uso:** Ejecutar las siguientes líneas de código (Nota: actualizar el valor de path_test con la imagen a analizar):

    model_url = "https://projectmlds-production.up.railway.app" 
    
    class ApiInput(BaseModel):
    features: List[List[List[float]]]
    
    path='benign_test.jpg'  #Actualizar path_test con la imagen a analizar.
    image_list = np.divide(np.array(Image.open(path).resize((300,300))), 255).tolist()
    
    inp = ApiInput(features=image_list)
    r = requests.post(
        os.path.join(model_url, "predict"),
        json=inp.dict(),
        )
    print(r.json()) 

11 **Instrucciones de mantenimiento:** Revisar cada 6 meses si las imagenes están siendo clasificadas correctamente, en caso contrario re-entrenar el modelo.


