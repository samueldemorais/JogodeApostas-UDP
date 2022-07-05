#Código do cliente LSD
import socket
from aposta import apostador, apostas
import threading


def cadastrar(nome):

    print (f'=========oi {nome}, bem vindo a MEGA-SENA LSD=========')
    # A = input('qual o seu nome de apostador?')
    # B = input("qual o valor da sua aposta?")
    # C = input("Informe a 1° dezena:")
    # D = input("Informe a 2° dezena:")
    # E = input("Informe a 3° dezena:")
    # F = input("Informe a 4° dezena:")
    # G = input("Informe a 5° dezena:")
    A = "KKK"
    B = '100'
    C = '22'
    D = '23'
    E = '24'
    F = '25'
    G = '26'
    dados = "DADOS" + " " + A + "," + B + "," + C + "," + D + "," + E + "," + F + "," + G
    udp.sendto(dados.encode(), servidor)
    #msg_servidor, serv = udp.recvfrom(1024)
    #print(msg_servidor.decode())
        
print('====== LISTA DE COMANDO ======= \nCAD   ---- Cadastrar novo usuário \nPLAY  ---- jogar na Mega-sena LSD \nSHOW  ---- Mostrar os resultados \nRESET ---- resetar jogo \nSAIR  ---- encerrar o programa')


def recebimento():
    while True:
        print('Lendo:', udp.getsockname())
        msg_servidor, servidor = udp.recvfrom(1024)
        print('Recebi:', msg_servidor.decode())
        mensagem_servidor = msg_servidor.decode().split(",")
        print(mensagem_servidor[0])

        if mensagem_servidor[0] == "ERROR DEBORA":
            print("Não há apostadores suficentes")

        if mensagem_servidor[0] == "ERROR LOUISE":
            print("Comando digitado não é reconhecido")

        if mensagem_servidor[0] == "ERROR WAGNER":
            print("Pontuação Máxima foi 0 e não houve ganhador")

        if mensagem_servidor[0] == "OK JUNIOR":
            print("O jogo foi resetado com sucesso")

        if mensagem_servidor[0] == "OK GUSTAVO":
            print(f"Números sorteados: {mensagem_servidor[1:]}")

        if mensagem_servidor[0] == "OK SAMUEL":
            print("======RESULTADO=======")
            print(f'ganhador:{mensagem_servidor[1]}')
            print(f'pontuação:{mensagem_servidor[2]}')
            print(f'prêmio total:{mensagem_servidor[3]}')

        if mensagem_servidor[0] == "OK LEONIDAS":
            print("Cadastro realizado com sucesso")

def envio():
    while True:
        msg = input("LSD>>>")
        mensagem = msg.split()
        command = mensagem[0].upper()
        if command == "CAD":
            cadastrar(mensagem[1])
        
        else:
            udp.sendto(msg.encode(), servidor)
            # msg_servidor, servidor = udp.recvfrom(1024)
            # mensagem_servidor = msg_servidor.decode().split(",")
            # print(mensagem_servidor[0])
            # if mensagem_servidor[0] == "ERROR DEBORA":
            #     print("Não há apostadores suficentes")
            # if mensagem_servidor[0] == "ERROR LOUISE":
            #     print("Comando digitado não é reconhecido")
            # if mensagem_servidor[0] == "ERROR WAGNER":
            #     print("Pontuação Máxima foi 0 e não houve ganhador")
            # if mensagem_servidor[0] == "OK JUNIOR":
            #     print("O jogo foi resetado com sucesso")
            # if mensagem_servidor[0] == "OK GUSTAVO":
            #     print(f"Números sorteados: {mensagem_servidor[1:]}")
            # if mensagem_servidor[0] == "OK SAMUEL":
            #     print("======RESULTADO=======")
            #     print(f'ganhador:{mensagem_servidor[1]}')
            #     print(f'pontuação:{mensagem_servidor[2]}')
            #     print(f'prêmio total:{mensagem_servidor[3]}')
            # if mensagem_servidor[0] == "OK LEONIDAS":
            #     print("Cadastro realizado com sucesso")

# deixar dinâmico o ip            
HOST = '127.0.0.1'
PORT = 40000

cliente = ("0.0.0.0", 0)
servidor = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(cliente)

thread_recebimento = threading.Thread(target = recebimento)
thread_recebimento.start()
thread_envio = threading.Thread(target = envio)
thread_envio.start()

