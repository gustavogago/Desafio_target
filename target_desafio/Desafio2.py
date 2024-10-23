string = input("Digite a Frase: ")

contador = 0

for caractere in string:
    if caractere.lower() == 'a':
        contador += 1


print("A letra 'a' aparece ",contador," vezes na string.")

