#Medio corto todo...

def main() -> None:
    while True:
        n = int(input("Ingrese un número: "))
        if n > 0:
            break

    lista = [x **2 for x in range(1, n+1)]

    #print(lista)
    print(lista[-10: ])


if __name__ == "__main__":
    main()    