def distancia_hamming(cadena1, cadena2):
    # Aseguramos que las cadenas tengan igual longitud
    if len(cadena1) != len(cadena2):
        return float('inf')  # Si no tienen la misma longitud, no se pueden comparar
    return sum(c1 != c2 for c1, c2 in zip(cadena1, cadena2))

def determinar_similitud_hamming(lista_original, numero_nuevo, umbral=2):
    numero_cadena = str(numero_nuevo)
    menor_distancia = float('inf')
    numero_mas_parecido = "nuevo"

    for numero in lista_original:
        distancia = distancia_hamming(str(numero), numero_cadena)
        if distancia < menor_distancia:
            menor_distancia = distancia
            numero_mas_parecido = numero

    return numero_mas_parecido if menor_distancia <= umbral else "nuevo"

# Ejemplo de uso
lista_original = [2441006710, 5581023627]
entradas = [2441006711, 2244100671, 2451006710, 5558102362, 2244100871, 
            5227816305, 5282716305, 2441007611, 2441000675, 2441886770, 
            2414006710, 5527816305]

for numero in entradas:
    resultado = determinar_similitud_hamming(lista_original, numero)
    print(f"{numero} -> {resultado}")
