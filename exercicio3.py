def soma_dos_aninhados(listas_aninhadas):
    soma_total = 0
    for lista in listas_aninhadas:
        soma_total += sum(lista)
    return soma_total

# Teste a sua função aqui (caso ache necessário)

lista1 = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

resultado1 = soma_dos_aninhados(lista1)
resultado2 = soma_dos_aninhados(outra_lista)

print("Soma da lista1:", resultado1)
print("Soma da outra_lista:", resultado2)











