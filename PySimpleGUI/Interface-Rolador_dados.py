import PySimpleGUI as sg

class TelaRolaDados:
    def __init__(self):
        sg.change_look_and_feel('DarkTeal5')
        # ou theme(new_theme = None)
        #Layout
        layout = [
            [sg.Text('Clique em um dado para rolar.')],
            [sg.Radio('Normal','rolagem',key='normal'),sg.Radio('Vantagem','rolagem',key='vantagem'),sg.Radio('Desvantagem','rolagem',key='desvantagem'),],
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

    
    def Iniciar(self):
        while True:
            #Extrair dados da Tela
            self.button, self.values = self.janela.Read()        
            n_de_dados = self.values['n de dados']
        #    d4 = self.values['d4']
            normal = self.values['normal']
            vantagem = self.values['vantagem']
            desvantagem = self.values['desvantagem']
            print(f'n de dados: {n_de_dados}')
        #    print(f'd4: {d4}')
            print(f'normal: {normal}')
            print(f'vantagem: {vantagem}')
            print(f'desvantagem: {desvantagem}')

tela = TelaRolaDados()
tela.Iniciar()