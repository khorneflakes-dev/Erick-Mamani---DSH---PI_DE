import pandas as pd
from sqlalchemy import create_engine
# aqui cargo funciones que voy creando segun la necesidad de limpieza de los datasets
from funciones_limpieza import del_dashes, exctract_quantity, exctract_unity, clear_nombre



# cargando los datasets iniciales
df_sucursal = pd.read_csv('./Datasets/sucursal.csv')
df_producto = pd.read_parquet('./Datasets/producto.parquet')



# datasets de precios
df1 = pd.read_csv('./Datasets/precios_semana_20200413.csv', delimiter=',', encoding='utf-16')
df2 = pd.read_csv('./Datasets/precios_semana_20200518.txt', delimiter='|')
df3 = pd.read_json('./Datasets/precios_semana_20200503.json')


# limpiando el dataset de productos
df_producto['cantidad'] = df_producto['presentacion'].apply(lambda x: exctract_quantity(x))
df_producto['unidad'] = df_producto['presentacion'].apply(lambda x: exctract_unity(x))
df_producto['categoria1'] = df_producto['categoria1'].fillna(0)
df_producto['categoria2'] = df_producto['categoria2'].fillna(0)
df_producto['categoria3'] = df_producto['categoria3'].fillna(0)
df_producto['nombre'] = df_producto['nombre'].apply(lambda x: clear_nombre(x))
df_producto.drop('presentacion', axis=1, inplace=True)


# limpiando el primer dataset de precios
df1 = df1.dropna()
df1['producto_id'] = df1['producto_id'].apply(lambda x: del_dashes(x))
df1 = df1[['producto_id','sucursal_id','precio']]
df1 = df1.drop_duplicates()


# limpiando el segundo dataset de precios
df2['precio'] = df2['precio'].fillna(0)
df2 = df2.dropna()
df2 = df2[['producto_id','sucursal_id','precio']]
df2 = df2.drop_duplicates()


# limpiando el tercer dataset de precios
df3['producto_id'] = df3['producto_id'].apply(lambda x: del_dashes(x))
df3 = df3[['producto_id','sucursal_id','precio']]
df3 = df3.drop_duplicates()

precios_final = pd.concat([df1, df2, df3])
precios_final['precio'] = pd.to_numeric(precios_final['precio'])


# indicamos el motor de sql que usaremos y el nombre de la base de datos
# usamos sqlite para que pueda generar un archivo .db segun los requerimientos
engine = create_engine('sqlite:///proyecto_individual.db', echo=True)

# iniciamos la conexion
sqlite_connection = engine.connect()

# exportamos los datasets que ya tenemos tratados
df_producto.to_sql('producto', sqlite_connection, index=False, if_exists='fail')
df_sucursal.to_sql('sucursal', sqlite_connection, index=False, if_exists='fail')
precios_final.to_sql('precios', sqlite_connection, index='precio_id', if_exists='fail')
# cerramos la conexion
sqlite_connection.close()