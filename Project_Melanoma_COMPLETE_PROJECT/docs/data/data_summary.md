# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

En esta sección se presenta un resumen general de los datos. Se describe el número total de observaciones, variables, el tipo de variables, la presencia de valores faltantes y la distribución de las variables.

El dataset Melanoma Skin Cancer contiene imágenes con resolución 300x300 en RGB con un total de 10.000 imágenes, sin embargo, con el fin de buscar un mejor desempeño computacional en la implementación y ejecución del modelo, se decide ajustar el dataset a 5.000 imágenes. 

A continuación, se visualiza la cantidad total de imágenes. Tener en cuenta que el dataset origial está compuesto por dos carpetas llamadas test y train, y a su vez, dentro de cada una de estas, tienen dos carpetas llamadas benign y malignant.


![print](https://github.com/S4G0/project_mlds/blob/master/docs/data/screen_files.png)


![print](https://github.com/S4G0/project_mlds/blob/master/docs/data/screen_dataset.png)

Como se puede observar en el código anterior, incialmente se tiene 4 conjunto de datos posterior a cargar los datos, 4000 imágenes para entrenamiento (2.000 imágenes de melanomas benignos y 2.000 imágenes de melanomas malignos) y 1.000 imágenes para prueba (500 imágenes de melanomas benignos y 500 imágenes de melanomas malignos).

Luego del preprocesamiento y realizar el particionamiento del dataset en entrenamiento, validación en una proporción 80/20 y dejando la prueba con la misma cantidad de imágenes, obtenemos las siguientes cantidades:

![print](https://github.com/S4G0/project_mlds/blob/master/docs/data/screen_particio%CC%81n.png)

## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

No se encontraron datos faltantes o duplicados en el dataset descargado.

## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

Se puede observar a través del siguiente gráfico de barras que el dataset tienen una distribución homogénea en la variable objetivo, lo cual no será necesario aplicar alguna técnica de balanceo adicional en los datos:

![print](https://github.com/S4G0/project_mlds/blob/master/docs/data/screen_bar.png)

