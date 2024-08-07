import re

text = '''
Hola mundo.
Me gusta Python!!!!!!!!
Mi primer numero de la suerte es 987-654-321
Mi primer numero de la suerte es 123-456-789
Mi primer numero de la suerte es 765-432-100
Mi primer numero de la suerte es 876-543-543-543-210
'''

# Buscar el primer emparejamiento
# print(re.search(r'\d', text))
# print(re.search(r'hola', text, flags=re.IGNORECASE))

# buscar todos los emparejamientos
# print(re.findall(r'\d', text))

# Encontrar puntuación
# print(re.findall(r'[^\w\s]', text))

# Validar una fecha
text = '''
13-04-2022
2022-13-04
2022-04-13
'''

# print(re.findall(r'\d{2}-\d{2}-\d{4}', text))

# Validar un usuario
# Condicion: de 4-14 y solo numeros o letras

text = '''
usuario10
abc
10
'''

print(re.findall(r'[a-z0-9]{4,14}', text))
