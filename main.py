from fastapi import FastAPI
import uvicorn
import pyarrow
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

app=FastAPI(debug=True)

DataSet_Final_A = pd.read_parquet('DataSet_Final2.parquet', engine='pyarrow')
DataSet_Final =pd.DataFrame(DataSet_Final_A)

@app.get('/')
def message():
    return 'PROYECTO INTEGRADOR ML OPS de Hevert Daniel Martinez (agregar /docs al enlace para acceder a las funciones / add /docs to link to access features)'


@app.get('/developer/') 
async def developer(desarrollador: str):
    Dev = DataSet_Final[DataSet_Final['developer'] == 'Valve']
    items = Dev[['anio', 'items_count']].groupby('anio').sum()
    countitems = Dev[['anio', 'items_count']].groupby('anio').count()
    ceros = Dev[Dev['price'] == 0]
    sceros = ceros[['anio', 'price']].groupby('anio').count()
    items['PorcentajeFree'] = (sceros['price']/countitems['items_count'])*100
    items['PorcentajeFree']=items['PorcentajeFree'].round(2)
    r = items.fillna(0)
    r=r.to_dict()
    return {"DataFrame":r}


@app.get('/user_data/')
async def userdata( User_id : str ):
    df_filtrado = DataSet_Final.loc[DataSet_Final["user_id"]== User_id]
    total_items= df_filtrado['item_id'].nunique()
    porcentaje_recomendacion= (df_filtrado['recommend'].sum() / total_items) * 100
    cantidad_dinero= df_filtrado['price'].sum()
    return {f'usuario':User_id, 'porcentaje de recomendacion':porcentaje_recomendacion, 'dinero gastado':cantidad_dinero}

@app.get('/UserForGenre/')
async def UserForGenre(genero: str) -> dict:
    fg= DataSet_Final[DataSet_Final['genres'] == genero]
    fg2 = fg[['user_id', 'playtime_forever']].groupby(fg['user_id']).sum()
    r1 = fg2['playtime_forever'].idxmax()
    cA= fg[fg['user_id'] == r1]
    r2 = cA['anio'].groupby(cA['anio']).sum()

    return {f'Usuario con más horas jugadas para Género ':r1, 'Años ':r2.to_dict()}

@app.get('/best_developer_year/')
async def best_developer_year(año: int):
    # Filtrar el dataset por el año especificado
    year_data = DataSet_Final[DataSet_Final['anio'] == año]

    # Contar la cantidad de juegos recomendados por desarrollador para el año dado
    developer_recommendations = year_data['developer'].value_counts()

    # Obtener los top 3 desarrolladores con más juegos recomendados
    top_3_developers = developer_recommendations.head(3)

    # Construir la lista de retorno
    return [{"Puesto 1": top_3_developers.index[0]}, 
            {"Puesto 2": top_3_developers.index[1]}, 
            {"Puesto 3": top_3_developers.index[2]}]


@app.get('/develorper_reviews_analysis/')
async def developer_reviews_analysis(desarrolladora: str) -> dict:
    Dev = DataSet_Final[DataSet_Final['developer'] == desarrolladora]['Sentimiento']
    r1 = (Dev == 2).sum()
    r2 = (Dev == 1).sum()
    r3 = (Dev == 0).sum()
    r = r1 + r2
    return {f'Desarrollador ':desarrolladora, 'Positivo ':r.tolist(), 'Negativo':r3.tolist()}



def recomendacion(id_producto: int):
    # Inicializar el vectorizador TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    ml = DataSet_Final.head(4000)
# Vectorizar la descripción de los juegos
    tfidf_matrix = vectorizer.fit_transform(ml['review'])


    if id_producto not in muestra['steam_id'].values:
        return {'mensaje': 'No existe el id del juego.'}
    
    # Obtener géneros del juego con el id_producto
    generos = muestra.columns[2:17]  # Obtener los nombres de las columnas de género
    
    # Filtrar el dataframe para incluir juegos con géneros coincidentes pero con títulos diferentes
    filtered_df = muestra[(muestra[generos] == 1).any(axis=1) & (muestra['steam_id'] != id_producto)]
    
    # Calcular similitud del coseno
    tdfid_matrix_filtered = tfidf.transform(filtered_df['reviews'])
    cosine_similarity_filtered = linear_kernel(tdfid_matrix_filtered, tdfid_matrix_filtered)
    
    idx = muestra[muestra['steam_id'] == id_producto].index[0]
    sim_cosine = list(enumerate(cosine_similarity_filtered[idx]))
    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True)
    sim_ind = [i for i, _ in sim_scores[1:6]]
    sim_juegos = filtered_df['title'].iloc[sim_ind].values.tolist()
    
    return print({'juegos recomendados': list(sim_juegos)})



