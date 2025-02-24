# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

MelanomAI: Un Proyecto de Inteligencia Artificial para Detectar Melanoma Cutáneo

## Objetivos del Proyecto

    • Desarrollar un modelo de aprendizaje automático capaz de identificar y clasificar de manera precisa las imágenes de melanoma en el conjunto de datos.
    • Optimizar el modelo para minimizar los errores, especialmente los falsos positivos y falsos negativos, mejorando así la confiabilidad de la detección.
    • Asegurarse de que el modelo sea capaz de generalizar su capacidad de detección a imágenes de melanoma no vistas previamente, garantizando así su aplicabilidad en situaciones del mundo real.

## Alcance del Proyecto

### Descripción de los Datos Disponibles:
El proyecto se basará en el conjunto de datos de Melanoma Skin Cancer de Kaggle, que consta de 10,000 imágenes. Cada imagen está etiquetada como "benigna" o "maligna", proporcionando la base para el aprendizaje supervisado. Los datos incluyen información sobre características específicas de las lesiones cutáneas, como tamaño, forma y color. 

### Descripción de los Resultados Esperados:
    • Desarrollar un modelo de aprendizaje automático capaz de clasificar imágenes de lesiones cutáneas como benignas o malignas con una alta precisión.
    • Presentar métricas de evaluación, como precisión, para validar la eficacia del modelo.
    
### Criterios de Éxito del Proyecto:
Precisión del Modelo: Se espera alcanzar una precisión del modelo superior al 80%, asegurando una clasificación confiable de las imágenes.
Generalización: El modelo debe ser capaz de generalizar su capacidad de detección a nuevas imágenes de melanoma no incluidas en el conjunto de entrenamiento.
Interpretabilidad: Lograr una explicación comprensible y transparente de las decisiones del modelo para garantizar la confianza de los usuarios, especialmente en entornos médicos.
Eficiencia Computacional: El modelo debe ser eficiente en términos de tiempo de procesamiento, permitiendo su aplicación en entornos clínicos y de atención médica en tiempo real.

## Metodología

### Entendimiento del negocio y carga de datos:
    • Familiarización con el conjunto de datos de Kaggle, comprendiendo las características de las imágenes y las etiquetas asociadas.
    • Investigación sobre las características clínicas relevantes para la detección de melanoma.
### Análisis exploratorio:
    • Análisis exploratorio de datos para entender la distribución de las clases, la variabilidad en las características y posibles desafíos.
    • Visualización de imágenes para identificar patrones visuales distintivos.
### Preprocesamiento de Datos:
    • Normalización de las imágenes para asegurar consistencia en la escala de píxeles.
    • División del conjunto de datos en conjuntos de entrenamiento, validación y prueba.
    • Manejo de desequilibrios de clase, si los hay, mediante técnicas como sobremuestreo o submuestreo, batches, entre otros.
### Modelamiento y extracción de características:
    • Selección de un modelo base (tales como redes neuronales convolucionales (CNN), Transformers, modelos pre-entrenados y fine tuning) adecuado para la tarea de clasificación de imágenes.
    • Entrenamiento del modelo utilizando el conjunto de entrenamiento y validación.
    • Ajuste de hiperparámetros para mejorar el rendimiento del modelo.
### Despliegue y Evaluación del Modelo:
    • Evaluación del modelo en el conjunto de prueba para medir su rendimiento en datos no vistos.
    • Análisis de métricas de evaluación, tales como la precisión.
    • Interpretación de los resultados para comprender las fortalezas y debilidades del modelo.
    • Optimización y Ajuste Fino:
    • Identificación de áreas de mejora basadas en los resultados de la evaluación.
    • Ajuste fino del modelo para abordar deficiencias identificadas.


## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | Del 7-14 de noviembre de 2023. |
| Preprocesamiento, análisis exploratorio | 1 semana  | Del 14-21 de noviembre de 2023. |
| Modelamiento y extracción de características | 1 semana  | Del 21-28 de noviembre de 2023. |
| Despliegue | 1 semana  | Del 28 de noviembre al 5 de diciembre de 2023. |
| Evaluación y entrega final | 1 semana  | Del 1-8 de diciembre de 2023. |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

    • Santiago Gómez Arias	sagomezar@unal.edu.co  (Realiza el envío)
    • Diana Paola Montes Grajales	dmontesgrajales@gmail.com
    • Mario Alberto Najar Martínez	donteo06@gmail.com 

## Presupuesto

No aplica.

## Stakeholders

Científicos de Datos: Responsables del desarrollo y entrenamiento del modelo de aprendizaje automático.
Dermatólogos: Especialistas en piel que pueden proporcionar información clínica, validar los resultados del modelo y ofrecer perspectivas sobre la aplicabilidad en entornos clínicos.
Médicos Generales: Usuarios finales que podrían utilizar el sistema como una herramienta de apoyo en la detección temprana de melanoma.
Pacientes: Beneficiarios finales del proyecto, ya que una detección temprana y precisa puede mejorar los resultados y el tratamiento del melanoma.

## Aprobaciones
Dr. Jorge Eliecer Camargo Mendoza, Ph.D.
Oscar Alberto Bustos, MSc.
