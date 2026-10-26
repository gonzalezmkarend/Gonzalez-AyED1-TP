for x in range(10_001):
    try:
        print(x)

    except KeyboardInterrupt:
        while True:
            num = int(input("\nPresione 1 para salir. 2 para continuar: "))
            if num == 2:
                for j in range(x + 1, 10_001):
                    print(j)

            if num == 1:
                print("\nConteo cancelado.")
                break
        break
