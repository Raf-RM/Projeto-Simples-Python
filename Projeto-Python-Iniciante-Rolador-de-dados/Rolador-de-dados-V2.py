import random

class Dado:
    def __init__(self,numero_de_faces):
        self.n = numero_de_faces
    
    def rola_dado(self):
        self.rolagem = random.choice(list(range(1,self.n+1)))
        print("resultado",self.rolagem)

