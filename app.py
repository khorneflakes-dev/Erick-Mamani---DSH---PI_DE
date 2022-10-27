import pandas as pd

# definiendo las funciones de limpieza
# para el dataset que que viene en formato csv
def del_dashes(value):
    value = str(value)
    list_value = value.split('-')
    return list_value[-1]

def exctract_quantity(value):
    value = str(value)
    list_value = value.split(' ')
    return (list_value[0])

def exctract_unity(value):
    value = str(value)
    list_value = value.split(' ')
    return list_value[-1]


def format_productoId(value):
    if len(str(value)) < 13:
        value_formated = '0'*(15 - len(str(value))) + str(value)
        return value_formated
    else:
        return str(value)

df1 = pd.read_csv('./Datasets/precios_semana_20200413.csv', delimiter=',', encoding='utf-16')
df2 = pd.read_csv('./Datasets/precios_semana_20200518.txt', delimiter='|')
df3 = pd.read_json('./Datasets/precios_semana_20200503.json')
df4 = pd.read_excel('./Datasets/precios_semanas_20200419_20200426.xlsx')
# df = pd.read_csv('./Datasets/sucursal.csv')
df_producto = pd.read_parquet('./Datasets/producto.parquet')

# print(df[df['producto_id']=='9-3-0000000962155'])

# print(df.dtypes)
# df['producto_id'] = pd.to_numeric(df['producto_id'])

# # limpiando el primer dataset de precios
# df1 = df1.dropna()
# df1['producto_id'] = df1['producto_id'].apply(lambda x: del_dashes(x))
# # df1['producto_id'] = pd.to_numeric(df1['producto_id'])
# df1 = df1[['producto_id','sucursal_id','precio']]

# limpiando el segundo dataset de precios
df2['precio'] = df2['precio'].fillna(0)
df2 = df2.dropna()
df2 = df2[['producto_id','sucursal_id','precio']]

# limpiando el tercer dataset de precios
df3['producto_id'] = df3['producto_id'].apply(lambda x: del_dashes(x))
df3 = df3[['producto_id','sucursal_id','precio']]

# limpiando el cuarto dataset de precios
df4['producto_id'] = df4['producto_id'].astype(int)
df4['producto_id'] = df4['producto_id'].apply(lambda x: format_productoId(x))
print(df4.dtypes)
print(df4)

# limpiando el dataset de productos
df_producto['presentacion_cantidad'] = df_producto['presentacion'].apply(lambda x: exctract_quantity(x))
df_producto['presentacion_unidad'] = df_producto['presentacion'].apply(lambda x: exctract_unity(x))
df_producto['categoria1'] = df_producto['categoria1'].fillna(0)
df_producto['categoria2'] = df_producto['categoria2'].fillna(0)
df_producto['categoria3'] = df_producto['categoria3'].fillna(0)
