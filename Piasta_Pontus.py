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

print ('Czas lotu ciała wyniósł: ',(wzory.czas(h)),'[s]')
print ('Zasięg lotu wyniósł: ',(wzory.zasieg(v,h)),'[m]')
print ('Równanie toru ruchu ma postać: ',(wzory.rownanie(v,h)))









#print(czas)
#print(zasieg)
#print(rownanie)

# print('Wyniki') 17.12.2020r.

# wykres (17.12.2020r.)
# plt.plot(x,y,color='r', lw=1, ls='-', label='wzorek')
# plt.legend()
# plt.xlabel('X', fontsize = 8)
# plt.ylabel('f(x)', fontsize = 8)
# plt.show()


# Zapis do pliku (17.12.2020r.)
# np.savetxt('wyniki.dat',a)
