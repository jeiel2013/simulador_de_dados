import random
import time

print("Bem vindo ao Simulador de Dados!")
print("Estaremos sorteando os seus números em 5 segundos!")

num_aleat_prim = random.randint(1,6)
num_aleat_sec = random.randint(1,6)

def countdown(tempo):
    for i in range(tempo, 0, -1):
        print(i)
        time.sleep(1)  # Pausa por 1 segundo
    print("Tempo esgotado!")

tempo_para_contagem = 5  # Altere para o tempo desejado em segundos
countdown(tempo_para_contagem)

print("\nSeu primeiro número é: ", num_aleat_prim)
print("Seu segundo número é: ", num_aleat_sec)