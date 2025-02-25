=======
# Sistema de recomendación - prueba técnica
Este proyecto implementa un sistema de recomendación usando FastAPI para el despliegue y Docker para contenerizar la aplicación. Se utilizó UV para hacer la gestión de dependencias.


---
## Explicación del dataset y procesamiento de datos
El dataset se compone de 3 archivos de texto plano en formato CSV con la información de los usuarios, los productos, y las interacciones entre los usuarios con los productos.

El dataset de usuarios (users.csv) contiene los siguientes campos:
```
user_id: Identificador único del usuario.                           edad: Edad del usuario                                        genero: Género del usuario.	
nivel_ingresos: Nivel de ingresos.                                  nivel_educativo: Nivel educativo.                             intereses: Lista de intereses separados por comas.
tipo_suscripcion: Tipo de suscripción.                              categoria_cliente: Categoría del cliente.                     ubicacion: Ubicación del usuario.
dispositivo: Dispositivo principal de acceso.                       frecuencia_login: Frecuencia con la que el usuario inicia sesión.
```
En el modelo solo se usaron los campos de usuario "user_id", "edad",	"genero" e "intereses", ya que se consideró que "nivel de ingresos", "nivel_educativo", "tipo_suscripcion", "categoría_clientes", "ubicacion", "dispositivo" y "frecuencia login" eran variables que no nos aportaban mucha información sobre las preferencias de los clientes. Y a la variable edad se le hizo una transformación a una variable categórica agrupándo la edad en bines de 12, es decir se agruparon las edades de [18 a 29], [30,41], [42,53], [54,65], [66,77] y [78,89]. Se usó un agrupado uniforme ya que la variable de edad estaba unifórmemente distribuida.

El dataset de productos (products.csv) contiene los siguientes campos:
```
product_id: Identificador único del producto o servicio.   	        name: Nombre del producto o servicio.                         category: Categoría del producto.	
descripcion: Descripción del producto o servicio.          	        palabras_clave: Palabras clave relacionadas con el producto. 	precio: Precio del producto o servicio en dólares.	
rating_promedio: Puntuación promedio del producto.                  descuento_aplicado: Descuento aplicado en porcentaje.         stock_actual: Número de unidades disponibles en stock.
```
En el modelo solo se usaron los campos de productos "product_id", "name", "category", "descripcion" y "palabras_clave", ya que se consideró que "precio", "descuento_aplicado" y "stock_actual" eran variables que no describían intrinsicamente las características del producto o servicio. A la variable "palabras_clave" se le realizó una pequeña transformación donde se organizaron las distintas palabras clave de forma alfabética, es decir si tenemos las palabras clave "Rendimiento, Deporte, Fitness" se transforma a "Deporte, Fitness, Rendimiento". Después de esa transformación se evidenció que había una gran cantidad de productos y servicios duplicados, hay en realidad solo 15 servicios/productos diferentes. Por lo que se creó un campo llamado "index" para identificar estos servicios/productos de forma única.

El dataset de interacciones (interactions.csv) contiene los siguientes campos:
```
user_id: Identificador del usuario que interactuó con un producto.  metodo_pago: Método de pago utilizado.                        tipo_interaccion: Tipo de interacción.	
rating: Puntuación otorgada al producto.                   	        comentario: Opinión del usuario sobre el producto.            timestamp: Fecha y hora de la interacción.	
product_id: Identificador del producto con el que el usuario interactuó. 
```
En el modelo solo se usaron los campos de interacciones "user_id",	"product_id",	"tipo_interaccion", "rating" y "comentario", ya que se consideró que "método_pago" no era una variable relevante para el modelo de recomendación y "timestamp" tampoco fue relevante ya que todas las interacciones se encuentran en un periodo corto de tiempo entre 2023-01-01 y	2023-02-04. Se mapearon 4 tipos de interacciones mediante el campo "tipo_interaccion" los cuales fueron comentario, compra, consulta y valoración. Los campos con tipo de interacción igual a "consulta" se eliminaron ya que no hay forma de evaluar la experiencia del usuario con dicho producto, y con el tipo de interacción igual a "compra" en este caso se decidió eliminar estos registros. Aunque en otros casos podríamos decir que si un usuario compra un servicio es porque le interesa bastante entonces significaría una calificación máxima, esto se debería discutir con el negocio de como manejar estos casos. En el tipo de interacción igual a "valoración, el campo "rating" no era nulo, y tenía valores enteros entre 1 y 5, de aqui extraíamos la apreciación de los usuarios con respecto a los usuarios. Y con el tipo de interacción igual a "comentario" el campo comentario exhibía los valores Excelente, Podría mejorar, Aceptable, Malo, Recomendado, para poder unificar estos valores con los del tipo de interacción igual a "valoración" se decidió hacer un reemplazo donde  Excelente, Recomendado, Podría mejorar, Aceptable, Malo y   los reemplazabamos por 5, 5, 3, 3 y 1 respectivamente. Finalmente ya unificados estos campos hicimos un reescalamiento de estos valores para llevarlos de un rango entre 1 a 5 a un rango de 0 a 1, usando un max-min scaler. Finalmente se hizo un join con la tabla transformada de productos para obtener el campo "index" el cual es el identificador único de producto.


---
## Metodología utilizada para generar recomendaciones
Para hacer las recomendaciones se implementaron tres sistemas de recomendación:

**Sistema de recomendación basado en popularidad:** Este sistema de recomendación se base en agrupar al usuario con base en sus intereses, edad y género (si no reportaba genero o era no binario solo se hacía de acuerdo a edad e intereses) y se calcula cuales son los productos/servicios más populares para este grupo. Y con base en esto se hace la recomendación.

**Sistema de recomendación de filtro basado en contenido:** En este sistema de recomendación calculamos la similitud entre los productos que el usuario ya compró anteriormente con respecto a otros productos que no ha comprado, basado en características tales como las palabras clave y la categoría a la que el producto pertenece, luego asignamos una calificación a cada producto que no ha comprado el usuario basada en la similitud con los productos que el usuario compro ya enteriormente y la calificación dada por el usuario, y los productos no comprados con mayor puntuación son los que se recomiendan.

**Sistema de recomendación de filtro colaborativo:** Este sistema de recomendación calcula la similitud entre diferentes usuarios con base en los productos en comun y sus calificaciones, después de calcular esta correlación entre todos, se toman los usuarios con mayor correlación al usuario que se desea hacerle la recomendación, y luego se calcula una calificación para cada producto basado en la correlación que tienen los usuarios que compraron ese producto con el usuario objetivo y todo esto pesado con la calificación de los usuarios. Ya habiendo calculado estas calificaciones, los productos con mayor calificación son los que se recomiendan.

Finalmente como el modelo devuelve solo 3 productos recomendados, entonces cada sistema de recomendación devuelve 3 productos para recomendar, y lo que se trata de hacer es recomendar los productos que más se repiten en los diferentes sistemas de recomendación. Si hay un producto que se repite en los 3 sistemas seguro es recomendado. Sin embargo si no existiera ningun producto que se repite se toma el producto de primer lugar de cada recomendador.


---
## Estructura del Proyecto
```
Project_Recommendation_system/
│── docker-compose.yaml                    # Archivo de docker compose
│── README.md                              # Documentación del proyecto
│── pruebas_API.png                        # Imagen con pruebas de funcionamiento de la API
│── API/                                   # Carpeta con los archivos del servicio de API
│──── api.py                               # Implementación de la API con FastAPI
│──── requirements.txt                     # Dependencias necesarias para la API
│──── Dockerfile                           # Dockerfile para contenerizar la API
│──── modelo.py                            # Archivo de python con el **MODELO DE RECOMENDACIÓN**
│── ML/                                    # Carpeta con los archivos del servicio de transformación de datos
│──── EDA_y_transformacion_de_datos.ipynb  # Notebook de **PRE-PROCESAMIENTO DE DATOS** que genera los archivos de la carpeta data/
│──── requirements.txt                     # Dependencias necesarias para la transformación de datos
│──── Dockerfile                           # Dockerfile para contenerizar el modelo de ML
│──── interactions.csv                     # Data inicial de interacciones
│──── products.csv                         # Data inicial de productos
│──── users.csv                            # Data inicial de usuarios
│── data/                                  # Carpeta de volumen de datos NO volátiles
│──── interactions_tr.csv                  # Datos de interacciones transformado creado por el notebook EDA_y_transformacion_de_datos.ipynb de la carpeta ML/
│──── products_tr.csv                      # Datos de productos transformado creado por el notebook EDA_y_transformacion_de_datos.ipynb de la carpeta ML/
│──── users_tr.csv                         # Datos de usuarios transformado creado por el notebook EDA_y_transformacion_de_datos.ipynb de la carpeta ML/
```


---
## Este proyecto fue desarrollado utilizando las siguientes tecnologías y librerías

- Python 3.9: Lenguaje de progrmación escogido para hacer el procesamiento de datos, desarrollar el modelo y desplegar con FastAPI
- FastAPI: Tecnología escogida para realizar el despliegue
- Scikit-Learn y NumPy: Librerías de Python que fueron necesarias para realizar ciertos cálculos (Cosine_similarity por ejemplo) o manipulaciones de datos
- Pandas: Librería de Python central para realizar la manipulación de las bases de datos mediante dataframes.
- Docker: APlicación para crear contenedores y así tener entornos totalmente controlados para poder desplegar servicios
- Jupyter y Jupyter notebook: Mediante los notebook de Python se da mejor visibilidad a ciertos cálculos o partes del código
- UV: Gestor de dependencias


---
## Instrucciones para poder usar la API

### 1. Clonar el Repositorio
Si tenemos GIT, a través de GIT bash podemos clonar la carpeta del sistema de recomendación mediante los siguientes comandos
```
git init
git remote add origin https://github.com/S4G0/PersonalProjectsPublic.git
git config core.sparseCheckout true
git sparse-checkout set Project_Recommendation_system
git pull origin main
```
O también podemos descargar el repositorio en un comprimido ZIP y quedarnos con la carpeta Project_Recommendation_system

### 2. Ejecución servicio de API en contenedor de Docker
Entramos a la carpeta que clonamos o descargamos en el paso anterior, es decir a Project_Recommendation_system.
Iniciamos el servicio que nos va a permitir usar la API, lo cual es necesario tener docker para poder ejecutar el siguiente comando
```
sudo docker compose up api_service
```
Este servicio va a desplegar la API en el puerto 5000 de nuestro local_host.

### 3. Uso de la API
Teniendo el servicio en ejecución podemos en la terminal ejecutar 
```
curl -X GET "http://localhost:5000/recommendations?user_id=123"
```
o en nuestro navegador meternos al url ```http://localhost:5000/recommendations?user_id=123```
donde 123 lo reemplazaríamos con el user_id del usuario con el que deseamos hacer la recomendación de contenido.


---
## Ejemplos de ejecuciones de la API
![pruebas](./pruebas_API.png)


---
## Análisis sobre el rendimiento del modelo y posibles mejoras
### Tiempo de inferencia:
El tiempo de inferencia del modelo es de unos pocos segundos. 
### Áreas de mejora del modelo:
El sistema de recomendación se podría complementar usando modelos basados en redes neuronales, sin embargo hay que tener en cuenta que esto podría impactar en el tiempo de inferencia si se usan redes neuronales muy grandes.
El sistema de recomendación basado en contenido se podría mejorar usando embeddings u otro método de modelado semántico para aprovechar la descripción del producto/servicio y así usar esta información para calcular las similitudes entre los diferentes productos.
### Métricas de rendimiento del modelo:
Para hacer este análisis se podrían proponer métricas para medir el desempeño de este modelo en producción mediante un A/B testing.


