import tensorflow as tf

# Verificar si TensorFlow detecta una GPU
print("GPU disponible:", tf.config.list_physical_devices('GPU'))

# Ejemplo simple de multiplicación de matrices
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
result = tf.matmul(a, b)
print("Resultado de la multiplicación de matrices:")
print(result.numpy())
# Resultado de la multiplicación de matrices:
# [[19 22]
#  [43 50]]