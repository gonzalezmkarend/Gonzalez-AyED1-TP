
def centrar_caracteres(texto: str) -> None:
    '''
    Contrato: Imprime texto centrado en 80 columnas.
    
    Precondiciones: La variable que recibe debe ser string.
    Postcondiciones: No devuelve nada, solo se encarga de hacer un print.
    
    '''
    #texto = texto.center(80)
    #print(texto)

    largo = len(texto)

    if largo < 80:
        espacio = 80 - largo
        esp = espacio // 2
        print(" " * esp + texto + " " * esp)

    elif largo == 80:
        print(texto)

    else:
        for i in range(0, largo, 80):
            print(texto[i:i+80])


centrar_caracteres('Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk, agh burzum-ishi krimpatul')

centrar_caracteres('One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them')

centrar_caracteres('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

centrar_caracteres('11111111111111111111') #Si la cadena tiene menos de 80 caracteres la centra.