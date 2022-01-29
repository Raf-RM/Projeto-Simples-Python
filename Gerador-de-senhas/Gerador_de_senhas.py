import PySimpleGUI as sg
import random

class TelaGeradorSenha:
    # -- PARTE RESPONSÁVEL POR CRIAR A PARTE GRÁFICA DO PROGRAMA
   
    def __init__(self):
    # -- CONSTRUTOR DA CLASSE
        
        layout = [
            [sg.Text('Escolha o(s) tipo(s) de caracter(es) para compor a nova senha. ')],
            [sg.Checkbox('Letras', key = 'letras'),sg.Checkbox('Números', key = 'numeros'),sg.Checkbox('Caracteres', key = 'caracteres')],
            [sg.Text('Site:'), sg.Input(key='site')],
            [sg.Text('Loggin:'), sg.Input(key='loggin')],
            [sg.Text('Número de Caracteres:'), sg.Input(size=(4,0), default_text=1, key='tamanho')],
            [sg.Button('Gerar')]]
        self.janela = sg.Window('Rolador de Dados').layout(layout)

    def GeradorAleatorio(self,lista):
    # -- SELECIONA UM ITEM ALEATÓRIO DE UMA LISTA

        self.aleatorio = random.choice(lista)
        return self.aleatorio
    
    def Construcao(self, tamanho, letras = None, numeros = None, caracteres = None):
    # -- CONSTROI A SENHA COM STRINGS GERADAS ALEATORIAMENTE PODENDO CONTER LETRAS E/OU NÚMEROS E/OU CARACTERES ESPECIAIS      

        lista_letras_total =['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
        lista_numeros = ['0','1','2','3','4','5','6','7','8','9']
        lista_especiais = ['!','?','@','#','$','%','&']
        senha = ''

        if letras and not numeros and not caracteres:
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_letras_total)
        elif numeros and not letras and not caracteres:
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_numeros)
        elif caracteres and not numeros and not letras:
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_especiais)
        elif letras and numeros and not caracteres:
            lista_total = lista_letras_total + lista_numeros
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_total)
        elif letras and caracteres and not numeros:
            lista_total = lista_letras_total + lista_especiais 
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_total)
        elif caracteres and numeros and not letras:
            lista_total = lista_numeros + lista_especiais 
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_total)
        elif letras and numeros and caracteres:
            lista_total = lista_letras_total + lista_numeros + lista_especiais 
            for i in range(int(tamanho)):
                senha = senha + gera.GeradorAleatorio(lista_total)
        return senha

    def GravarArquivo(self, site, senha, loggin = None,):
    # -- GRAVA A SENHA GERADA EM UM ARQUIVO (EXISTENTE OU NÃO)

        arquivo = open ('arq_s.txt','a')
        arquivo.write(site + '\n')
        arquivo.write(loggin + '\n')
        arquivo.write(senha + '\n')
        arquivo.write('\n')
        arquivo.close() 
 

    def Iniciar(self):
    # -- INICIA O PROGRAMA LÊ AS ENTRADAS E CHAMA AS DEMAIS FUNÇÕES

        while True:
            self.event, self.values = self.janela.Read()
            letras = self.values['letras']
            numeros = self.values['numeros']
            caracteres = self.values['caracteres']
            site_saida = self.values['site']
            loggin_saida = self.values['loggin']
            n_caracteres = self.values['tamanho']

            senha = gera.Construcao(n_caracteres, letras, numeros, caracteres)
            gera.GravarArquivo(site_saida, senha, loggin_saida)

    # -- FALTA FAZER:
    # -- GARANTIR QUE HAJA AO MENOS 1 CARACTERE PARA CADA TIPO ESCOLHIDO (LETRAS, NÚMEROS E CARACTERES ESPECIAIS)
    #    DE ACORDO COM O NÚMERO DE CARACTERES DEFINIDO
    # -- GARANTIR QUE O MESMO SITE/LOGGIN NÃO SEJA REGISTRADO COM SENHAS DIFERENTES. 
           

gera = TelaGeradorSenha()
gera.Iniciar()