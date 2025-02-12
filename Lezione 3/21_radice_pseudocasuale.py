import math
import random
numero = random.randint(10, 1000)
radice_quadrata = math.sqrt(numero)
radice_arrotondata = round(radice_quadrata, 3)
print("Numero generato:", numero)
print("Radice quadrata arrotondata:", radice_arrotondata)