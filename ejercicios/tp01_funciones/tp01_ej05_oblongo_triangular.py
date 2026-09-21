
# ---Lambda de oblongo:
oblongo = lambda num: ((4 * num + 1) ** (1 / 2)) % 1 == 0

# ---Lambda triangular:
triangular = lambda num: ((1 + 8 * num) ** (1 / 2)) % 1 == 0

while True:
    num = int(input("Ingrese un número: "))
    if num > 0:
        break

es_oblongo = oblongo(num)

if es_oblongo == True:
    print(f"El número {num} es oblongo.")

else:
    print(f"El número {num} no es un oblongo.")

es_triangular = triangular(num)
if es_triangular == True:
    print(f"El número {num} es triangular.")

else:
    print(f"El número {num} no es triangular")

assert oblongo(12) == True
assert oblongo(10) == False
assert triangular(15) == True
assert triangular(11) == False
