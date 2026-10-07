
def muestra_listado(pacientes: list[tuple]) -> None:
    '''
    Contrato: Muestra dos listas de aquellos pacientes que fueron atendidos por urgencia y por turno.
    
    pre: las lístas dentro de la tupla no deben estar vacías.
    post: Imprime por pantalla los pacientes por orden de llegada.
    
    '''
    urgencia = []
    turno = []
    
    for p, a in pacientes:
        if a == 0:
            urgencia.append(p)
            
        elif a == 1:
            turno.append(p)
            
    if len(urgencia) > 0:
        print("\nPACIENTES DE URGENCIA:")
        for urg in urgencia:
            print(urg)
            
    else:
        print("\nNo se atendieron pacientes de urgencia.")
        
    if len(turno) > 0:
        print("\nPACIENTES CON TURNO:")
        for tur in turno:
            print(tur)


def historial_paciente(paciente: int, pacientes: list[tuple[int,int]]) -> tuple:
    """
    Contrato: Permite buscar el número de afiliado de un paciente y muestra cuantas veces fue atendido.
    
    pre: la variable paciente debe ser entera y positiva. Las listas de la tupla no deben estar vacías.
    post: Muestra por pantalla el historial de atención del paciente solicitado.
    
    """
    turno = 0
    urgencia = 0
    
    for pac, at in pacientes:
        if paciente == pac:
            if at == 0:
                urgencia += 1
            else:
                turno += 1
                
    return turno, urgencia   

def main() -> None:
    """
    Contrato: Función principal del programa desde la cual se ejecutan todas las funciones.
    
    pre: no recibe ningún dato.
    post: permite ingresar a los pacientes que son atendidos y ejecuta las funciones que muestran el listado de pacientes
    y la búsqueda de un historial individual.
    
    """
    pacientes = []
    
    while True:
        paciente = int(input("Ingrese el número de afiliado: "))
        if paciente == -1:
            break

        elif paciente >= 1000 and paciente <= 9999:
            while True:
                atencion = (int(input("Si es urgencia(0), turno(1): ")))

                if atencion in (0,1):
                    datos = paciente, atencion
                    pacientes.append(datos)
                    break
                    
    print(pacientes)                
    muestra_listado(pacientes)
    
    while True:
        busca_pac = int(input("Ingrese el número de afiliado(-1 para salir): "))
        if busca_pac == -1:
            break
        
        else:
            tur, urg = historial_paciente(busca_pac, pacientes)
            print(f"\nEl paciente: {busca_pac} fue atendido {tur} veces por turno y {urg} veces por urgencia.")
    

if __name__ == "__main__":
    main()