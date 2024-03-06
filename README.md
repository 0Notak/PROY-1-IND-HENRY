# PI_ML_OPS
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align=center><img src=https://www.folio3.ai/wp-content/uploads/2023/03/Asset-4-788x301.png><p>

## **Introducción:**
Este proyecto consiste en crear una API que utiliza un modelo de recomendación para Steam, una plataforma multinacional de videojuegos, basado en Machine Learning. El objetivo es crear un sistema de recomendación de videojuegos para usuarios. La API ofrece una interfaz intuitiva para que los usuarios puedan obtener informacion para el sistema de recomendacion y datos sobre generos o fechas puntuales. 

## **Herramientas Utilizadas**
+ Pandas
+ Matplotlib
+ Numpy
+ Seaborn
+ Wordcloud
+ NLTK
+ Uvicorn
+ Render
+ FastAPI
+ Python
+ Scikit-Learn

## Descripcion general

El proyecto individual Nº1 se centra en Machine Learning Operations (MLOps) y consiste en la creación de una API que utiliza un modelo de recomendación para Steam, una plataforma multinacional de videojuegos. El objetivo principal es desarrollar un sistema de recomendación de videojuegos para los usuarios de esta plataforma, proporcionando una interfaz intuitiva que les permita obtener información sobre el sistema de recomendación, así como datos sobre géneros o fechas específicas.

Para llevar a cabo este proyecto, se utilizaron una serie de herramientas y bibliotecas, entre las que se incluyen Pandas, Matplotlib, Numpy, Seaborn, Wordcloud, NLTK, Uvicorn, Render, y FastAPI, todas ellas ampliamente utilizadas en el análisis de datos y el desarrollo de aplicaciones web en Python.

El proceso seguido constó de varias etapas:

    ETL (Extracción, Transformación y Carga): 

    Despliegue de la API: 

    EDA (Exploratory Data Analysis): 

    Modelo de Machine Learning: 

En resumen, el proyecto combinó técnicas de análisis de datos, desarrollo web y Machine Learning para crear un sistema de recomendación de videojuegos que proporciona a los usuarios de Steam una experiencia personalizada y precisa. Las herramientas y bibliotecas utilizadas reflejan las prácticas estándar en el campo de la ciencia de datos y la ingeniería de software, proporcionando un enfoque integral para abordar el problema planteado.

## **Paso a paso:**
### 1. ETL

Realizamos un proceso de ETL (Extracción, Transformación y Carga) en el que extrajimos datos de diferentes fuentes, los transformamos según las necesidades del proyecto y los cargamos en un destino final para su análisis y uso posterior. Las herramientas primordiales utilizadas fueron python, pandas, scikit learn y FastApi

### 2. Deployment de la API

Creamos una API utilizando el módulo FastAPI de Python, creando 5 funciones para que puedan ser consultadas:


    -- def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. Ejemplo de retorno:

    Año 	Cantidad de Items 	Contenido Free
    2023 	50 	27%
    2022 	45 	25%
    xxxx 	xx 	xx%

    -- def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

Ejemplo de retorno: {"Usuario X" : us213ndjss09sdf, "Dinero gastado": 200 USD, "% de recomendación": 20%, "cantidad de items": 5}

    -- def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

    -- def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

    -- def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}
  
Luego realizamos el deployement de esta API utilizando Render. 
Las herramientas utilizadas fueron: Uvicorn, Render, FastAPI

### 3. EDA

Realizamos un proceso de EDA (Exploratory Data Analysis) en el que exploramos y analizamos los datos de manera exhaustiva con el objetivo de obtener insights, identificar patrones, tendencias y relaciones, y así tomar decisiones fundamentadas en base a la información obtenida. Intentando asi obtener alguna pista para crear nuestro modelo de ML
Las herramientas utilizadas fueron: Numpy, Pandas, Matplotlib, Seaborn, Wordcloud, NLTK

### 4. Modelo de Machine Learning

Realizamos un modelo de Machine Learning para generar recomendaciones juegoss, utilizando algoritmos y técnicas como la similitud del coseno y scikit-lear, con el fin de brindar recomendaciones personalizadas y precisas basadas en los gustos y preferencias de cada usuario.
 
 Si es un sistema de recomendación item-item:

    -- def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

Si es un sistema de recomendación user-item:

    -- def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.



La herramienta utilizada fue: Scikit-Learn con las librerias: TfidfVectorizer, linear_kernel, cosine_similarity
Tambien son consultables en la API
