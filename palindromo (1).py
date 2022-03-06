def palindromo():
    r = 'S'

    while r == 'S':
        x = input('Digite uma frase: ').replace(' ', '').upper()
        if x == x[::-1]:
            print('\33[7;30mO inverso de {} é {}.\33[m\n\33[7;30mA frase é um palíndromo!\33[m'.format(x,x[::-1]))
        else:
            print('\33[7;31m{} não é um palíndromo!\33[m'.format(x))

        r = input('S ou N: ').upper()

palindromo()



