"""
Projecte: Posa a prova els teus reflexos

En aquest joc, un LED s'encendrà després d'un temps aleatori i el jugador haurà de prémer un botó el més ràpidament possible. 
El joc enregistrarà el temps entre l'encesa del LED i el prem el botó, i després mostrarà aquest temps de reacció a la pantalla.
"""

# Cal fer l'adaptació del codi!!!
from gpiozero import Button, LED
from time import time, sleep
from random import randint

led = LED(17)
btn = Button(4)

while True:
  sleep(randint(1,10))
  led.on()
  start = time()
  btn.wait_for_press()
  end = time()
  led.off()
  print(end - start)
