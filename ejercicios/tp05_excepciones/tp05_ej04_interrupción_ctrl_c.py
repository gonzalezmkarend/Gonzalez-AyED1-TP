# Ahora si
for x in range(10_001):
    try:
        print(x)

    except KeyboardInterrupt:
        op = input("\nPresione S para salir. Enter para continuar: ")         

        if op.upper() == "S":
            print("\nConteo cancelado.")
            break
