import random;

class apostas:
    
    def __init__(self, jogador):
        self.jogador = jogador 


    def SortearNumeros(self):
        sorteados = []
        for aux in range(5):
            sorteio = random.randint(10, 30)
            while sorteio in sorteados:
                sorteio = random.randint(10, 30)
            sorteados.append(sorteio)
        return sorteados 

class apostador:
    def __init__(self, nome, aposta, cliente):
        self.nome = nome
        self.aposta = aposta
        self.cliente = cliente
        

    def imprimir(self):
        print(apostas)