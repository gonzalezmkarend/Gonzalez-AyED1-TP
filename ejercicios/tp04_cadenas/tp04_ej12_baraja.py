palos = ["Oros", "Copas", "Espadas", "Bastos"]

baraja = [f"{num} {palo}" for palo in palos for num in range(1, 11)]

baraja2 = [(num, palo) for palo in palos for num in range(1, 11)]

print(baraja2)
