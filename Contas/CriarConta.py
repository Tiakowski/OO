def gerar_numero():
    import random
    numero = str(random.randrange(100000))
    conta ="C" + numero
    return conta

def conferir_existencia(conta):
   contas = open("contas.txt","r")
   verificador = contas.read()
   existe = conta in verificador
   contas.close()
   return existe

def conta_nova():
    existe = True
    while existe:
        conta = gerar_numero()
        existe = conferir_existencia(conta)
    return conta

def criar_conta_nova():
    conta = conta_nova()
    with open("contas.txt","a") as contas:
        contas.write("\n")
        contas.write(conta)
    return conta
