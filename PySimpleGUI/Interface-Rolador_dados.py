#from email.policy import default
#from xml.dom.pulldom import default_bufsize
from xml.dom.pulldom import default_bufsize
import PySimpleGUI as sg
import random



class TelaRolaDados:
    def __init__(self):
        sg.change_look_and_feel('DarkTeal5')
        # ou theme(new_theme = None)
        #Layout
        layout = [
            [sg.Text('Clique em um dado para rolar.')],
            [sg.Radio('Normal','rolagem',default=True,key='normal'),sg.Radio('Vantagem','rolagem',key='vantagem'),sg.Radio('Desvantagem','rolagem',key='desvantagem'),],
            [sg.Text('Número de dados:'), sg.Input(size=(3,0),default_text=1,key='n de dados')],
            [sg.Button('d4',key='d4'),
            sg.Button('d6',key='d6'),
            sg.Button('d8',key='d8'),
            sg.Button('d10',key='d10'),
            sg.Button('d12',key='d12'),
            sg.Button('d20',key='d20'),
            sg.Button('d100',key='d100')],
            [sg.Output(size=(30,15))]
        ]
        #Janela
        self.janela = sg.Window('Rolador de Dados').layout(layout)

    def rola_dado(self,dado):
        self.rolagem = random.choice(list(range(1,int(dado[1:])+1)))
        return self.rolagem

    def Iniciar(self):
        while True:          
            #Extrair dados da Tela
            self.event, self.values = self.janela.Read()
            dado = self.event
            n_de_dados = int(self.values['n de dados'])
            normal = self.values['normal']
            vantagem = self.values['vantagem']
            desvantagem = self.values['desvantagem']
        
            if dado == 'd4' or 'd6' or 'd8' or 'd10' or 'd12' or 'd20' or 'd100':
                rolagem = []
                soma = 0

                if dado == 'd20' and vantagem:
                    for i in range(2):
                        rolagem.append(tela.rola_dado(dado))
                    if rolagem[0] > rolagem[1]:
                        print(f'{rolagem} = {rolagem[0]}')
                    else:
                        print(f'{rolagem} = {rolagem[1]}')
                elif dado == 'd20' and desvantagem:
                    for i in range(2):
                        rolagem.append(tela.rola_dado(dado))
                    if rolagem[0] < rolagem[1]:
                        print(f'{rolagem} = {rolagem[0]}')
                    else:
                        print(f'{rolagem} = {rolagem[1]}')                        
                
                if n_de_dados == 1 and normal:
                    rolagem.append(tela.rola_dado(dado))
                    print(f'{rolagem[0]}')
                elif n_de_dados > 1 and normal:
                    for i in range(n_de_dados):
                        rolagem.append(tela.rola_dado(dado))
                        soma += rolagem[i]
                    print(f'{rolagem} = {soma}')                

            print()        
#            print(f'n de dados: {n_de_dados}')
#            print(f'normal: {normal}')
#            print(f'vantagem: {vantagem}')
#            print(f'desvantagem: {desvantagem}')

tela = TelaRolaDados()
tela.Iniciar()