Comparación de Números por Similitud

Este proyecto implementa dos métodos para comparar números basándose en su similitud. Los algoritmos determinan si un número nuevo es similar a otros en una lista, utilizando dos enfoques diferentes: la distancia de Levenshtein y la distancia de Hamming.
Funciones principales

Distancia de Levenshtein
Este método mide el número mínimo de operaciones (inserciones, eliminaciones, sustituciones) necesarias para transformar una cadena en otra. Es más flexible, ya que permite comparar cadenas de longitud diferente, pero es más costoso en tiempo y memoria.
Distancia de Hamming
Este método cuenta los dígitos diferentes entre dos cadenas de igual longitud. Es más rápido y eficiente en memoria, pero solo funciona cuando las cadenas tienen la misma longitud.
