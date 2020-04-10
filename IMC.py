# coding=utf-8

print('=-' * 21)
print('Cálculo de Índice de massa corporal - IMC')
print('=-' * 21)


def imc():
    sair = 'C'
    vnome = False
    vsexo = False
    vpeso = False
    valtura = False
    vsair = False

    while sair != 'S':
        while vnome == False:
            nome = n1 = input('Digite o seu nome: ').upper()
            try:
                nome = nome.isalpha()
                if nome == True:
                    vnome = True
                else:
                    print ('NOME deve conter somente letras')
            except:
                print('NOME deve conter somente letras')

        while vsexo == False:
            sexo = input('Sexo - [M] Masculino [F]Feminino: ').upper()
            try:
                if sexo == 'M' or sexo == 'F' :
                        vsexo = True
                        #print(sexo)
                else:
                    print('SEXO deve optar por M ou F')
            except:
                  print('SEXO deve optar por M ou F')

        while vpeso == False:
            peso = input('Digite o seu peso: ')
            try:
                peso = float(peso)
                if peso > 0:
                    vpeso = True
                else:
                    print('PESO deve conter somente números e decimais separados por PONTO(.)')
            except:
                  print('PESO deve conter somente números e decimais separados por PONTO(.)')

        while valtura == False:
            altura = input('Digite a sua altura: ')
            try:
                altura = float(altura)
                if altura > 0:
                    valtura = True
                else:
                    print('ALTURA deve conter somente números e decimais separados por PONTO(.)')
            except:
                  print('ALTURA deve conter somente números e decimais separados por PONTO(.)')

        imc = peso / (altura ** 2)
        #print(imc)

        if sexo == 'M' and imc < 20.7:
            print(n1,', sexo:',sexo, '=> Abaixo do peso.')
        elif sexo == 'M' and imc < 26.4:
            print(n1,', sexo:',sexo, '=> Peso normal.')
        elif sexo == 'M' and imc < 27.8:
            print(n1, ', sexo:',sexo, '=> Marginalmente acima do peso!')
        elif sexo == 'M' and imc < 31.1:
            print(n1, ', sexo:',sexo, '=> Acima do peso ideal!')
        elif sexo == 'M' and imc > 31.1:
            print(n1,' ,sexo',sexo,'=> Você está o obeso!')
        elif sexo == 'F' and imc < 19.7:
            print(n1,' ,sexo',sexo,'=> Abaixo do peso.')
        elif sexo == 'F' and imc < 25.8:
            print(n1,' ,sexo',sexo, '=> Peso normal.')
        elif sexo == 'F' and imc < 27.3:
            print(n1, ' ,sexo',sexo,'=> Marginalmente acima do peso!')
        elif sexo == 'F' and imc < 32.3:
            print(n1, ' ,sexo',sexo,'=> Acima do peso ideal!')
        elif sexo == 'F' and imc > 32.3:
            print(n1, ' ,sexo',sexo,'=> Você está o obeso!')

        while vsair == False:
            sair = input('Digite [S] para sair ou [C] para continuar: ').upper()
            try:
                if sair == 'S' or sair == 'C':
                    vsair = True
                else:
                    print ('Digite S ou C.')
            except:
                print('Digite S ou C.')

        vnome = False
        vsexo = False
        vpeso = False
        valtura = False
        vsair = False

print(imc())

