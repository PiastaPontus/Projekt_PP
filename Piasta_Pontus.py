# Modelowanie - projekt, Nikodem Piasta, Robert Pontus
# Modelownie rzutu poziomego w polu grawitacyjnym.

import numpy as np
import matplotlib.pyplot as plt
import os
import math
import wzory

print('Oto program do symulacji ruchu poziomego z pewnej wysokośći H o danej prędkości początkowej V')

while True:
    try:
        h = float(input('Proszę podaj wysokość początkową ciała w metrach:'))
        break
    except ValueError:
        print("Wprowadzono błędny typ danych, spróbuj jeszcze raz")
while True:
    try:
        v = float(input('Proszę podaj wartość prędkości początkowej [m/s]:'))
        break
    except ValueError:
        print("Wprowadzono błędny typ danych, spróbuj jeszcze raz")


print('Dane:\n wysokość - h=', h, '[m]\n prędkość początkowa: v=', v, '[m/s]\n przyspieszenie ziemskie - g=', (wzory.g), '[m/s^2]\n\n')

print('Wyniki:\n')
print ('Czas lotu ciała wyniósł: ',round((wzory.czas(h)),3),'[s]')
print ('Zasięg lotu wyniósł: ',round((wzory.zasieg(v,h)),3),'[m]')
print ('Równanie toru ruchu ma postać: ',(wzory.rownanie(v,h)))


x=np.arange(0,10) #JAkoś tutaj przeskalować
y= h - ((9.81 * (x**2)) / (2*(v**2)))
plt.plot(x,y, color='r', lw=1, ls='-', label='Tor ruchu ciała')
plt.ylim(0)
plt.legend()
plt.xlabel('Odległość', fontsize = 8)
plt.ylabel('f(x)', fontsize = 8)
plt.savefig('wykres.jpg', dpi = 300)
plt.show()


#np.savetxt('wyniki.dat',a)
