import random


# Función que simula el juego del Monty Hall
# Recibe como parámetro un booleano que indica si el jugador cambia de puerta
# Retorna un booleano que indica si el jugador ganó o no
def MontyHall(change_door):
  #aleatoriedad de ubicación de auto
  doors = {1: False, 2: False, 3: False}
  winning_door = random.randint(1, 3)
  doors[winning_door] = True

  # aleatoriedad de elección de puerta
  player_choice = random.randint(1, 3)

  # aleatoriedad de elección de puerta del presentador.
  # si la puerta del presentador es la misma que la del jugador
  # o la puerta del presentador tiene un auto, se elige otra puerta
  host_choice = random.randint(1, 3)
  while (host_choice == player_choice or doors[host_choice] == True):
    host_choice = random.randint(1, 3)

  # análisis de cambio de puerta
  if (change_door == True):
    selected_doors = [host_choice, player_choice]
    doors_array = doors.keys()
    newdoor = list(set(doors_array) - set(selected_doors))
    player_new_door = newdoor[0]

    #print("Ganadora:", winning_door, ", Elegida:", player_choice, ", Abierta:",
    #      host_choice, ", Cambio a P:", player_new_door)

    return (winning_door == player_new_door)
  else:
    #print("Ganadora:", winning_door, ", Elegida:", player_choice, ", Abierta:",
    #      host_choice)
    return (winning_door == player_choice)


# Simulación de 1000 partidas

resultsTrue1000 = []
for i in range(1000):
  resultsTrue1000.append(MontyHall(True))

resultsFalse1000 = []
for i in range(1000):
  resultsFalse1000.append(MontyHall(False))

print("")
print("======================")
print("Frecuencia y frecuencia relativa con 1.000:")
print("======================")
print("Frecuencia de TRUE (cambiando de puerta):", resultsTrue1000.count(True))
print("Frecuencia relativa de TRUE (cambiando de puerta):", resultsTrue1000.count(True)/1000)

print("")
print("Frecuencia de FALSE (manteniendo la misma puerta):", resultsFalse1000.count(True))
print("Frecuencia relativa de FALSE (manteniendo la misma puerta):", resultsFalse1000.count(True)/1000)
print("")


# Simulación de 10000 partidas

resultsTrue10000 = []
for i in range(10000):
  resultsTrue10000.append(MontyHall(True))

resultsFalse10000 = []
for i in range(10000):
  resultsFalse10000.append(MontyHall(False))

print("")
print("======================")
print("Frecuencia y frecuencia relativa con 10.000:")
print("======================")
print("Frecuencia de TRUE (cambiando de puerta):", resultsTrue10000.count(True))
print("Frecuencia relativa de TRUE (cambiando de puerta):", resultsTrue10000.count(True)/10000)

print("")
print("Frecuencia de FALSE (manteniendo la misma puerta):", resultsFalse10000.count(True))
print("Frecuencia relativa de FALSE (manteniendo la misma puerta):", resultsFalse10000.count(True)/10000)
print("")

# Simulación de 100000 partidas

resultsTrue100000 = []
for i in range(100000):
  resultsTrue100000.append(MontyHall(True))

resultsFalse100000 = []
for i in range(100000):
  resultsFalse100000.append(MontyHall(False))

print("")
print("======================")
print("Frecuencia y frecuencia relativa con 100.000:")
print("======================")
print("Frecuencia de TRUE (cambiando de puerta):", resultsTrue100000.count(True))
print("Frecuencia relativa de TRUE (cambiando de puerta):", resultsTrue100000.count(True)/100000)

print("")
print("Frecuencia de FALSE (manteniendo la misma puerta):", resultsFalse100000.count(True))
print("Frecuencia relativa de FALSE (manteniendo la misma puerta):", resultsFalse100000.count(True)/100000)
print("")