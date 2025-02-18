import pandas as pd
datos = {
    'Nombre': ['Juan', 'Pedro', 'Ana', 'Luis', 'Maria'],
    'Edad': [25, 30, 20, 35, 22],
    'Sexo': ['M', 'M', 'F', 'M', 'F'],
    'Ciudad': ['Monte Vera', 'Recreo', 'Santa Fe', 'Paiva', 'Rafaela']
    }
df = pd.DataFrame(datos)
print(df)
#  Nombre  Edad Sexo      Ciudad
# 0   Juan    25    M  Monte Vera
# 1  Pedro    30    M      Recreo
# 2    Ana    20    F    Santa Fe
# 3   Luis    35    M       Paiva
# 4  Maria    22    F     Rafaela

# Una vez que tienes un DataFrame, puedes realizar muchas operaciones útiles. Por ejemplo, puedes seleccionar solo una columna utilizando el nombre de la columna como un atributo:
edad = df['Edad']
print(edad)
# 0    25
# 1    30
# 2    20
# 3    35
# 4    22
# Name: Edad, dtype: int64

# También puedes realizar filtrados utilizando una condición booleana:
mayores_de_30 = df[df['Edad'] > 30]
print(mayores_de_30)
#  Nombre  Edad Sexo Ciudad
# 3   Luis    35    M  Paiva

