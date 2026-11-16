from datetime import datetime
from tp08_ej01_fechas_horarios import verifica_fecha


def extiende_fecha(fecha: tuple[int], corte: int, meses: dict) -> str:
    """
    Contrato: Convierte una fecha expresada en enteros y la extiende con el
    formato: dia:int, mes:str, año: int (4 dígitos)

    Precondiciones: La tupla de fechas debe contener tres enteros y no deben
    ser negativos.
    El diccionario meses no debe estar vacío y sus claves deben ser enteros.
    La variable corte debe ser entera.
    Postcondiciones: Devuelve la fecha extendida en formato cadena.

    """
    dia, mes, anio = fecha

    if anio < corte:
        anio = 2000 + anio

    elif anio <= 99 and anio > corte:
        anio = 1900 + anio

    return f"{dia} de {meses[mes]} de {anio}"


def main() -> None:
    """Función principal del programa."""
    corte = 30
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    fecha = verifica_fecha()
    if fecha:
        extendida = extiende_fecha(fecha, corte, meses)
        print(extendida)


if __name__ == "__main__":
    main()
