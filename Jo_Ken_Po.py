#predra papel ou tesoura
from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
pc=randint(0,2)
print('''suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador= int(input(' qual sua jogada ?'))
#jo ken po
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('='*20)
print('o computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[jogador]))
print('='*20)
#quem ganha
if pc == 0:#pedra
    if jogador == 0:
        print('empate')

    elif jogador == 1:
        print('jogador ganhou')

    elif jogador == 2:
        print('jogador perdeu')

elif pc == 1:#papel
    if jogador == 0:
        print('jogador perdeu')

    elif jogador == 1:
        print('empate')

    elif jogador == 2:
        print('jogador ganhou')

elif pc == 2:#tesoura
    if jogador == 0:
        print('jogador ganhou')

    elif jogador == 1:
        print('jogador perdeu')

    elif jogador == 2:
         print('empate')


