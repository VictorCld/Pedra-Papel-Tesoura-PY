import random

def pedra_papel_tesoura(jogador1, jogador2):
  if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
    raise ValueError("Escolha inválida. As opções válidas são: pedra, papel, tesoura.")

  if jogador1 == jogador2:
    return 0  
  elif jogador1 == "pedra" and jogador2 == "tesoura":
    return 1  
  elif jogador1 == "papel" and jogador2 == "pedra":
    return 1  
  elif jogador1 == "tesoura" and jogador2 == "papel":
    return 1  
  else:
    return 2  

jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
op_jogador2 = ["pedra","papel","tesoura"]
jogador2 = random.choice(op_jogador2)
print("Jogador 1 escolheu",jogador1,"e o computador escolheu",jogador2)
resultado = pedra_papel_tesoura(jogador1, jogador2)

if resultado == 0:
  print("Empate!")
elif resultado == 1:
  print("Jogador 1 venceu!")
else:
  print("Computador venceu!")