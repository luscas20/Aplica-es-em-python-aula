print("Abrindo um arquivo")

try:
    open("teste pdf", 'w')
    print("Arquivo Aberto")

except FileNotFoundError as Erro:
    print("Arquivo Inexistente")
    print("descrição:", Erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("descrição", erro)

print("Término do Programa")
