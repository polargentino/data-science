import tensorflow as tf

# Crear dos constantes, cada una con el valor 1
a = tf.constant(1)
b = tf.constant(1)

# Sumar las constantes
resultado = a + b

# Imprimir el resultado
print("La suma es:", resultado.numpy())  # .numpy() para obtener el valor como número normal
