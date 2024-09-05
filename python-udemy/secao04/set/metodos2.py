# Comparação entre sets  ///  CONJUNTOS NA MAT
s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2 # Operador de uniao de sets '|'  forma um conjunto com os itens presentes em ambos os conjuntos
print(s3)

s3 = s1 & s2 #interseção // Apenas os itens presentes em ambos os conjuntos são contabilizados aqui (&)
print(s3)

s3 = s1 - s2 #Diferença // Remove os itens do set a direita do set a esquerda (-) "remove a intersecção"
print(s3)

s3 = s1 ^ s2 #diferença simetrica // Conta apenas os valores que estão presentes apenas em um conjunto, basicamente remove a intercessão do conjunto
print(s3)
