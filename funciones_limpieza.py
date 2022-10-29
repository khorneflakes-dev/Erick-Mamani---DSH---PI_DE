# definiendo las funciones de limpieza

def del_dashes(value):
    """
    elimina los strings de la columna producto_id y devuelve solo el id que deberia ser
    """
    value = str(value)
    list_value = value.split('-')
    return list_value[-1]

def exctract_quantity(value):
    """
    extrae la cantidad de la medida de la columna presentacion
    """
    value = str(value)
    list_value = value.split(' ')
    return list_value[0]

def exctract_unity(value):
    """
    extrae la unidad de medida de la cantidad de la columna presentacion
    """
    value = str(value)
    list_value = value.split(' ')
    return list_value[-1]

def format_productoId(value):
    """
    formatea el id del producto para que tenga 13 digitos
    antes: 123
    despues: 00000123
    """
    if len(str(value)) < 13:
        value_formated = '0'*(15 - len(str(value))) + str(value)
        return value_formated[:-2]
    else:
        return str(value[:-2])

def clear_nombre(value):
    """
    elimina la unidad y la cantidad redundantes en la columna nombres    
    """
    value = str(value)
    list_value = value.split(' ')
    return " ".join(list_value[:-2])
