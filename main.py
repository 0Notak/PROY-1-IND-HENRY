from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import api_functions as af

import importlib
importlib.reload(af)


app=FastAPI(debug=True)




@app.get('/')
def message():
    return 'PROYECTO INTEGRADOR ML OPS de Hevert Daniel Martinez (agregar /docs al enlace para acceder a las funciones / add /docs to link to access features)'


@app.get('/developer/') 
async def developer(desarrollador: str):
   return af.developer(desarrollador)


@app.get('/user_data/')
async def userdata( User_id : str ):
    return af.userdata(User_id)

@app.get('/UserForGenre/')
async def UserForGenre(genero: str) -> dict:
    return af.UserForGenre(genero)
    

@app.get('/best_developer_year/')
async def best_developer_year(año: int):
    return af.best_developer_year(año)


@app.get('/develorper_reviews_analysis/')
async def developer_reviews_analysis(desarrolladora: str) -> dict:
   return af.best_developer_year(desarrolladora)
    






@app.get('/recomendacion_id/{id_producto}')
async def recomendacion(id_producto: int):
    af.recomendacion(id_producto)