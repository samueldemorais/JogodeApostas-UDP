import socket
from aposta import apostador, apostas
from pathlib import Path

HOST = '0.0.0.0'
PORT = 40000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

print('Servidor no ar...')
numeros_apostados = []
dinheiro = []
nomes = []
pontos = []
clientes = []

def cadastrar(dados, cliente):
    clientes.append(cliente)
    print(dados)
    info = dados.split(",")
    print(info)
    usuario = apostador((info[0]), int(info[1]), cliente)
    dinheiro.append(usuario.aposta)
    nomes.append(usuario.nome)
    numeros = [int(info[2]), int(info[3]), int(info[4]), int(info[5]), int(info[6])]
    numeros_apostados.append(numeros)
    print(numeros_apostados)    
    print(dinheiro)
    print(nomes)
    print(pontos)
    if usuario.nome in nomes:
        resposta = "OK LEONIDAS"
        udp.sendto(resposta.encode(), cliente)
    print(clientes)
    
        
       

def jogar():
    if len(nomes) >= 2:
        jogo = apostas(apostador)
        ganha = jogo.SortearNumeros()
        resposta = (f'OK GUSTAVO, {ganha}')
        #udp.sendto(resposta.encode(), cliente)
        num = 0 
        for c in range(len(numeros_apostados)):
            cont = 0
            for i in range(5):
                for j in range(len(numeros_apostados[0])):
                    if ganha[i] == numeros_apostados[num][j]:
                        cont += 1
            num += 1    
            pontos.append(cont)
        exibir_resultado()

    else: 
        resposta =  ("ERROR DEBORA")
        udp.sendto(resposta.encode(), cliente)



def exibir_resultado():
    premio = 0

    for i in range(len(dinheiro)):
        premio += dinheiro[i]


    max_value = None
    max_idx = None

    for idx, num in enumerate(pontos):
        if (max_value is None or num > max_value):
            max_value = num
            max_idx = idx
    if max_value > 0:
        resposta = (f'OK SAMUEL, {nomes[max_idx]}, {max_value},  {premio}')
    if max_value == 0:
        resposta = 'ERROR WAGNER'
    for c in clientes:
        udp.sendto(resposta.encode(), c)
        print(resposta)
    

def reset(): 
    numeros_apostados.clear()
    dinheiro.clear()
    nomes.clear()
    pontos.clear()
    resposta = "OK JUNIOR"
    udp.sendto(resposta.encode(), cliente)


while True:
    msg, cliente = udp.recvfrom(1024)
    print('Recebi do cliente ', cliente, msg.decode())
    resposta = ''
    tokens = msg.decode().upper().split()
    command = tokens[0]
    if command == "SAIR":
        break
            
    elif command == "PLAY":
        game =  jogar()
    
    elif command == "SHOW":
        results = exibir_resultado()

    elif command == "RESET":
        resetar = reset()

    elif command == "DADOS":
        cadastro = cadastrar(" ".join(tokens[1:]), cliente)
    else:
       resposta =  "ERROR LOUISE"
       udp.sendto(resposta.encode(), cliente)

udp.close()