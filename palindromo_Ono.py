#KPC
#La finalidad del sig. codigo es validar si una palabra o frase es palíndromo.

def palindromo_ono(palabra):
    palabra= palabra.lower().replace(" ","")

    #con esta parte se va a comparar la palabra original con su version invertida
    return palabra==palabra[::-1]

#Hay que pedirle al usuario la palabra o frase
entrada= input("Hola, ingresa una palabra o frase ")

if palindromo_ono(entrada):
    print (f"La palabra {entrada} es palindromo")
else: 
    print (f"{entrada} no es palindromo")
