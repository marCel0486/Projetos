from PySimpleGUI import *

#criar layout
layout = [[Txt('' * 10)],
          [Text('', size = (15,1), font = ('Helvetica',18),
                text_color = 'black' , key = 'input')],
          [Txt('' * 10)],
          [ReadFormButton('c'), ReadFormButton('<<')],
          [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')],
          [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
          [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
          [ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')],
]
#definir a janela
form = FlexForm('CALCULADORA_PICA', default_button_element_size= (5,2),
                auto_size_buttons = False, grab_anywhere = False )
form.Layout(layout)

#resultado
Resultado = ''

#criando um loop infinito
while True :
    #Button Values
    button, value = form.Read()

    #verificando o valor dos botões
    if button == 'c':
        Resultado = ''
        form.FindElement('input').Update(Resultado)
    elif button == '<<':
        Resultado = Resultado[:-1]
        form.FindElement('input').Update(Resultado)
    elif len(Resultado) == 16:
        pass

    #Resultados
    elif button == '=':
        resposta = eval(Resultado)
        resposta = str(round(float(resposta), 3))
        form.FindElement('input').Update(resposta)
        Result = resposta

    #fechando a jenela
    elif button == 'Quit' or button == None:
        break
    else:
        Resultado += button
        form.FindElement('input').Update(Resultado)













