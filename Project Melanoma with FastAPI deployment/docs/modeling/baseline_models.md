# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

En este proyecto utilizamos un modelo de red neuronal convolucional (CNN) utilizando la biblioteca TensorFlow. La arquitectura consiste en tres capas convolucionales, cada una seguida por una capa de pooling para reducir las dimensiones. Se incorpora regularización mediante capas de dropout para prevenir el sobreajuste. La última capa densa tiene una función de activación ReLU y la capa de salida utiliza la activación sigmoid, indicando un problema de clasificación binaria (melanoma benigno=0, melanoma maligno=1). La arquitectura busca extraer características relevantes de las imágenes de entrada con dimensiones 300x300 y 3 canales de color, y finalmente, generar una predicción binaria. La cantidad de unidades en la capa densa probado fue de 32 (neurons_in_dense_layer=32) y la tasa de dropout de 0.2. Por su parte, la tasa de aprendizaje fue probada con un valor de 1e-2 y 1e-3, obteniendo mejores resultados para este último y por tanto es el que aparece la versión final.

## Variables de entrada

Las variables de entrada corresponden a imagenes de melanoma maligno y benigno de 300 x 300 pixeles representadas como vectores.

## Variable objetivo

La variable a predecir es el tipo de melanoma (benigno=0 y maligno=1), en nuestro dataframe incial esta variable toma el nombre de 'label'.

## Evaluación del modelo

### Métricas de evaluación

Las métricas utilizadas para evaluar el rendimiento del modelo son presición (accuracy) y pérdida. El accuracy indica la proporción de muestras clasificadas correctamente por el modelo en relación con el total de muestras evaluadas. Por su parte, la périda representa la distancia o discrepancia entre las predicciones del modelo y las etiquetas reales. 

### Resultados de evaluación
Loss=0.284460097
Accuracy=0.899999976

## Análisis de los resultados

El modelo utilizado tiene una arquitectura de red neuronal convolucional (CNN) utilizando TensorFlow y Keras. Entre las ventajas, se destaca la inclusión de capas convolucionales y de pooling para el procesamiento eficiente de datos de imágenes, así como la implementación de dropout para regularizar el modelo y prevenir el sobreajuste durante el entrenamiento. Consideramos que la elección de la función de activación ReLU es apropiada y se aplica una semilla (seed) para garantizar la reproducibilidad de los resultados. Sin embargo, también existen algunas desventajas, la simplicidad general de la estructura podrían limitar la capacidad del modelo para capturar patrones más complejos. La evaluación del modelo se basa en métricas generales como pérdida y precisión, pero una evaluación más detallada podría favorecer una mejor comprensión de su desempeño, por ejemplo usando una matriz de confusión u otras estrategias para la evaluación. Otros aspectos que se pudieran mejorar a través de la experimentación, podría ser la arquitectura y el uso de diferentes hiperparámetros.

## Conclusiones

En términos de rendimiento, el modelo baseline muestra prometedores resultados con una pérdida (Loss) de 0.2844 y una precisión (Accuracy) de 0.9 en el conjunto de datos de entrenamiento. Estos valores indican una buena capacidad del modelo para minimizar la pérdida y clasificar correctamente el 90% de las muestras de entrenamiento. Sin embargo, a pesar de estos resultados iniciales positivos, aún existen oportunidades para mejorar el modelo. Las áreas de posible mejora incluyen la ajustar la arquitectura de la red, explorar diferentes configuraciones de hiperparámetros y realizar una evaluación más detallada en un conjunto de datos de prueba independiente. Este enfoque permitirá determinar la capacidad del modelo para generalizar a nuevos datos y proporcionará una evaluación más completa de su rendimiento en escenarios del mundo real.

## Referencias

-Melanoma Skin Cancer Dataset. Kaggle, 2023. Disponible en: https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images
-Curso Metodologías para el desarrollo de aplicaciones con Machine Learning, Universidad Nacional de Colombia, 2023.
