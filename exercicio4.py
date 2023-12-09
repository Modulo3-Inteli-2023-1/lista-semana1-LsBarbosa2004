def tem_duplicados(lista):
    # Usando um conjunto para rastrear elementos únicos
    elementos_unicos = set()

    for elemento in lista:
        if elemento in elementos_unicos:
            return True
        else:
            elementos_unicos.add(elemento)

    return False

# Teste sua função aqui (caso ache necessário)
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 1, 1, 1, 1]

resultado1 = tem_duplicados(lista1)
resultado2 = tem_duplicados(lista2)

print("Lista1 tem duplicados:", resultado1)
print("Lista2 tem duplicados:", resultado2)
