from random import randint
v=0
while True :
    jogador =int(input('diga um valor :'))
    computador= randint(0,11)
    total=jogador + computador
    tipo=' '
    while tipo not in 'PI':
       tipo=str(input('par ou impar ? [P/I]')).strip().upper()[0]
    print('voce jogou {} e computador {}. total de {}.'.format(jogador,computador,total))
    if tipo == 'p':
        if total % 2 == 0:
            print('voce ganhou !!!')
            v += 1
        else:
            print('voce perdeu !!!')
            break
    elif tipo == 'I' :
        if total %2 == 1:
            print('voce perdeu !!!')
            v += 1
        else :
            print('voce perdeu !!!')
            break
    print('vamos jogar novamente ?')
print('GAME OVER! voce venceu {} vezes .'.format(v))








