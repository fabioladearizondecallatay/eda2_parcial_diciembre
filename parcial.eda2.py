"""El código compara un número nuevo con una lista de números, 
utilizando la distancia de Levenshtein para medir cuán similares son. 

La función distancia_levenshtein calcula la mínima cantidad de operaciones necesarias 
(inserción, eliminación, sustitución) para transformar una cadena en otra. 

Luego, determinar_similitud encuentra el número más similar en la lista y verifica si 
su distancia es menor o igual al umbral definido. Si no hay coincidencia suficientemente cercana, 
el número se considera "nuevo"."""


def distancia_levenshtein(cadena1, cadena2):
    m, n = len(cadena1), len(cadena2)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                matriz[i][j] = j
            elif j == 0:
                matriz[i][j] = i
            else:
                costo = 0 if cadena1[i - 1] == cadena2[j - 1] else 1
                matriz[i][j] = min(
                    matriz[i - 1][j] + 1,  # Eliminación
                    matriz[i][j - 1] + 1,  # Inserción
                    matriz[i - 1][j - 1] + costo  # Sustitución
                )
    return matriz[m][n]

def determinar_similitud(lista_original, numero_nuevo, umbral=2):
    numero_cadena = str(numero_nuevo)
    menor_distancia = float('inf')
    numero_mas_parecido = "nuevo"

    for numero in lista_original:
        distancia = distancia_levenshtein(str(numero), numero_cadena)
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
    resultado = determinar_similitud(lista_original, numero)
    print(f"{numero} -> {resultado}")
