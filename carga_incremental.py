import pandas as pd
from sqlalchemy import create_engine
# cargando las funciones necesarias para limpiar el dataset nuevo
from funciones_limpieza import format_productoId

# como este archivo de precios viene en formato excel y este trabaja un poco mas lento
# lo cambiamos a csv y trabajamos con esa base:
# df4 = pd.read_excel('./Datasets/precios_semanas_20200419_20200426.xlsx')
# df4.to_csv('./Datasets/precios_semanas_20200419_20200426.csv')

# cargando el nuevo dataset
df4 = pd.read_csv('./Datasets/precios_semanas_20200419_20200426.csv')

# limpiando el cuarto dataset de precios
df4['producto_id'] = df4['producto_id'].astype(str)
df4['producto_id'] = df4['producto_id'].apply(lambda x: format_productoId(x))
df4 = df4[['producto_id','sucursal_id','precio']]
df4['precio'] = pd.to_numeric(df4['precio'])

# indicamos el motor de sql que usaremos y el nombre de la base de datos
# usamos la misma configuracion que en la carga inicial
engine = create_engine('sqlite:///proyecto_individual.db', echo=True)

# iniciamos la conexion
sqlite_connection = engine.connect()

# exportamos los datasets que ya tenemos tratados
# en este caso usamos el valor append en el parametro if_exists
# para que adicione valores a los ya existentes
df4.to_sql('precios', sqlite_connection, index='precio_id', if_exists='append')
# cerramos la conexion
sqlite_connection.close()