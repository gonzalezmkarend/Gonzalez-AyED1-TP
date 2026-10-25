while True:
    clave_maestra = input("\nIngrese la clave maestra: ")

    if clave_maestra.isdigit():
        clave_par = clave_maestra[1::2]
        clave_impar = clave_maestra[::2]
        break

    else:
        print("\nDebe ingresar dígitos.")

print(clave_impar)
print(clave_par)
