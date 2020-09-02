frase = 'Curso em Vídeo Python'

print(frase[3])
# Mostra só a letra na posição 3

frase = 'Curso em Vídeo Python'
print(frase[3:13])
# Mostra da posição 3 até a 12 (não conta a ultima posição)

frase = 'Curso em Vídeo Python'
print(frase[:13])
# Mostra do inicio até o 12

frase = 'Curso em Vídeo Python'
print(frase[13:])
# Mostra do 13 até o final

frase = 'Curso em Vídeo Python'
print(frase[1:15:2])
# Mostra do 1 até o 14 pulando de 2 em 2

frase = 'Curso em Vídeo Python'
print(frase[1::2])
# Mostra do 1 até o final pulando de 2 em 2

frase = 'Curso em Vídeo Python'
print(frase[::2])
# Mostra do inicio até o final pulando de 2 em 2

print("""Texto grannnnnnnnnnnnnnn
nnnnnnnnnnnnnnn
nnnnnnddddddeeeeeeeeee
eeeeeeeeeeeeeeeeeee""")
# Imprime a string pulando linhas

print(frase.count('o'))
# Mostra quantos o tem na string

print(frase.upper())
# Altera a string para maisculo
# lower para minusculo

print(len(frase))
# Mostra quantos caracteres tem a string (length)

print(frase.strip())
# Remove todos espaços vazios no inicio e no final da string

print(frase.replace('Python', 'Android'))
# Substitui python por android somente nesse print, não na string
# para substituir na string: frase = frase.replace('Python', 'Android')

print(frase.find('Video'))
# Imprime a posição da primeira letra da palavra procurada, se ela existir na sting
# Se não achar a palavra, retorna -1

print(frase.split())
# Separa as palavras da string em uma lista e só imprime

# dividido = frase.split()
# Separa a string em uma lista definitivamente para a string 'dividido'

# print(dividido[2][3])
# Mostra a letra na posição 3 (quarta letra) da palavra na posição 2 da lista (terceira palavra)

