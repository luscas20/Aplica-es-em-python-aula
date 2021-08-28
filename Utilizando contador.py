frase = "Eu amo comer amoras no café da manhã"
#resultado contando diretamente sem o split.
print("Contagem direta: ", frase.count("amo"))

#resultado usando a contagem com o split
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo== "amo":
        contador += 1
print("Contagem usando o spli + contador: ", contador)
