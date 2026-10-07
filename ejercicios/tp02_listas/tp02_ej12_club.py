
def ingresa_socio() -> list[int]:
    '''
    Contrato: Permite el registro de los socios.
    
    Pre: No recibe ningún dato.
    Post: Devuelve una lista de enteros que corresponden a los números de socio.
    
    '''
    socios = []
    while True:
        socio = int(input("\nIngrese el número de socio(5 dígitos): "))
        if socio == 0:
            print("\nFinalizó el registro de socios.")
            break
        
        elif socio >= 10_000 and socio <= 99_999:
            socios.append(socio)
            
        else:
            print("\nOpción inválida.")
            
    return socios
            

def informe_socios(lista_socios: list[int]) -> None:
    '''
    Contrato: Muestra por pantalla la cantidad de visitas de socios por día.
    
    Pre: La lista no debe estar vacía.
    Post: No devuelve nada, imprime por pantalla la información.
    
    '''
    for soc in set(lista_socios):
        veces = lista_socios.count(soc)
        print(f"\nEl socio: {soc} visitó la instalación {veces} veces.")
    


def borrar_socio(socio: int, lista_socios: list[int]) ->None:
    '''
    Contrato: Borra el registro de un socio y todas sus visitas.
    
    Pre: La variable socio debe ser un entero positivo y la lista socios no debe estar vacía.
    Post: No devuelve nada, solo elimina uno o más valores correspondientes al
    número de socio de la lista de socios.
    
    '''
    if socio in lista_socios:
        #for elem in lista_socios:
         #   if elem == socio:
          #      lista_socios.remove(elem)

        lista_socios = [elem for elem in lista_socios if elem != socio] 
        
        print(f"\nEl socio nro {socio} fue eliminado exitosamente.")
        #print(lista_socios)
    
    else:
        print(f"\nEl socio {socio} no se encontró en el registro.")


def main() -> None:
    '''
    Contrato: Función principal.
    
    pre: No recibe ningún parámetro.
    Post: Ejecuta por pantalla el registro de los socios, el informe de ingreso y la opción
    de borrar el registro de socio.
    
    '''
    
    lista_socios = ingresa_socio()
    informe_socios(lista_socios)
    
    while True:
        socio = int(input("\nIngrese el socio que desee eliminar: "))
        if socio >= 10_000 and socio <= 99_999:
            borrar_socio(socio, lista_socios)
            break
        
        else:
            print("\nEl número ingresado es inválido.")
            
            
if __name__ == "__main__":
    main()



