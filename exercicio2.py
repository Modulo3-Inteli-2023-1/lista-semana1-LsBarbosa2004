def cumulativo(lista):
    soma_cumulativa = 0
    resultado_cumulativo = []
    for numero in lista:
        soma_cumulativa += numero
        resultado_cumulativo.append(soma_cumulativa)
    return resultado_cumulativo

# Teste a sua função aqui (caso ache necessário)
listaexemplo = [2, 3, 4, 5]
resultado = cumulativo(listaexemplo)
print(listaexemplo)
print(resultado)
