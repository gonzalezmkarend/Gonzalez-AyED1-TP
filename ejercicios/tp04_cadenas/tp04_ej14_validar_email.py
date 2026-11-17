def valida_mail(mail: str) -> str | None:
    """
    Contrato: Recibe un mail y verifica si este es válido.
    Un mail es válido cuando:
        Tiene un único @
        El usuario es alfanumérico
        El dominio debe tener al menos un carácter
        Debe finalizar en .com o .com.ar

    Precondiciones: La variable mail debe ser una cadena.
    Postcondiciones: Si el mail es válido devuelve su dominio.
    En caso de ser inválido no retorna nada.

    """
    mail = mail.casefold()

    contador = mail.count("@")
    if contador != 1:
        return

    mail = mail.split("@")
    usuario = mail[0]
    dominio = mail[1]

    if usuario.isalnum():
        if dominio.endswith(".com") and len(dominio) > len(".com"):
            return dominio

        elif dominio.endswith(".com.ar") and len(dominio) > len(".com.ar"):
            return dominio

    else:
        return


def main() -> None:
    """Función principal"""

    correos = {}
    while True:
        mail = input(
            "\nIngrese un correo electrónico (presione enter sin texto para salir): "
        )
        if mail:
            mail_validado = valida_mail(mail)

            if mail_validado:
                correos.add(mail_validado)

        else:
            print("\n------Lista de dominios------")
            for correo in sorted(correos):
                print(correo)
            break


if __name__ == "__main__":
    main()
