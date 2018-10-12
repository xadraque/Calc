#instancia o valor da varialvel que ira receber o valor da operaçãp
valor=0
#inicia um laço de repitição permanente
while True:
    #instancia variaveis para outros laços de repições
    ver = False
    ver2 = False

    #enquanto valor da operação = a zero inicia a operação com a digitação dos dos numeros
    if(valor ==0):
    #solicita ao usuario que digite um operador pra fazer a operação ou que o mesmo digite "q" para sair do lope
        op = input("Qual Operação (+, -, *, /) você deseja fazer OU \'q\' para Sair: ")

    #condição que para o loop permante
        if(op=="q" or op=="Q"):
            break
    #Condição para continuar a operação
        elif(op=="+"or op=="-" or op=="*"or op=="/"):

        #Caso a condição acima seja atendida inicia um laço de repitição até que o usuario digite um numero valido
            while ver==False:
            #tratamento de execeção
                try:
                    n1 = float(input("Digite o primeiro numero da operação: "))
                    ver=True #Se o Usuario digitar um numero valido troca o valor da Variavel e encerra o laço de repitição
                except ValueError:#Se ditidado o valor que não seja um numero valido da a mensagem de erro e retorno ao inicio da repitição
                    print("Deu erro!!! \nDigite um numero valido")

        # Caso a condição acima seja atendida inicia um laço de repitição até que o usuario digite um numero valido
            while ver2 == False:
            # tratamento de execeção
                try:
                    n2 = float(input("Digite o segundo numero da operação: "))
                    ver2=True#Se o Usuario digitar um numero valido troca o valor da Variavel e encerra o laço de repitição
                except ValueError:#Se ditidado o valor que não seja um numero valido da a mensagem de erro e retorno ao inicio da repitição
                    print("Deu erro de conversão \nDigite um numero valido")

    #Caso o usuario digite um operador invalido da a mensagem de erro e reinicia o loope
        else:
            Total = "Operação não Existe!!!"
            print(Total)

    # Só entra na conta caso seja digitado o operador correto e os numeros validos
    # Operadores que fazem as operações.
        if (op=="+"):
            total=n1+n2
            print(total)
        elif(op=="-"):
            total=n1-n2
            print(total)
        elif(op=="*"):
            total=n1*n2
            print(total)
        elif(op=="/"):
            total=n1/n2
            print(total)
        print("\nO Valor da Operação ", n1, op, n2, ": ", total)  # imprime a operação feita e o valor

    #caso valor não seja zerado continua a conta a partir do valor obtido na conta anterior
    else:

        # solicita ao usuario que digite um operador pra fazer a operação ou que o mesmo digite "q" para sair do lope
        op = input("Qual Operação (+, -, *, /) você deseja fazer OU \'q\' para Sair: ")

    #condição que para o loop permante
        if(op=="q" or op=="Q"):
            break
    #Condição para continuar a operação
        elif(op=="+"or op=="-" or op=="*"or op=="/"):

        #Caso a condição acima seja atendida inicia um laço de repitição até que o usuario digite um numero valido
            while ver==False:
            #tratamento de execeção
                try:
                    n1 = float(input("Digite o proximo valor da operação: "))
                    ver=True #Se o Usuario digitar um numero valido troca o valor da Variavel e encerra o laço de repitição
                except ValueError:#Se ditidado o valor que não seja um numero valido da a mensagem de erro e retorno ao inicio da repitição
                    print("Deu erro!!! \nDigite um numero valido")

    #Caso o usuario digite um operador invalido da a mensagem de erro e reinicia o loope
        else:
            Total = "Operação não Existe!!!"
            print(Total)

    # Só entra na conta caso seja digitado o operador correto e os numeros validos
    # Operadores que fazem as operações.
        if (op=="+"):
            total=valor+n1
            print(total)
        elif(op=="-"):
            total=valor-n1
            print(total)
        elif(op=="*"):
            total=valor*n1
            print(total)
        elif(op=="/"):
            total=valor/n1
            print(total)
        print("\nO Valor da Operação ",valor,op,n1,": ",total)#imprime a operação feita e o valor

    #solicita ao usuario se quer zerar e recomeçar a conta ou continuar de onde parou
    n= input("\nDeseja zerar a conta se Sim digite \'S\': ")

    #atribui o valor que o usuario solicitou anteriormente, se disse sim zera a variala valor, se não atribui o total a variavel valor
    if(n=="s" or n=="S"):
        valor=0
    else:
        valor=total