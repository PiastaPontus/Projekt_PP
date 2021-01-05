# Modelowanie - projekt, Nikodem Piasta, Robert Pontus
# Modelownie rzutu poziomego w polu grawitacyjnym.

import numpy as np
import matplotlib.pyplot as plt
import os
import math
import wzory

print('Oto program do symulacji ruchu poziomego z pewnej wysokośći H o danej prędkości początkowej V')

#Pobieranie danych
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

#Wzory z pliku zew.
czas = wzory.czas(h)
zasieg = wzory.zasieg(v,h)
rownanie = wzory.rownanie(v,h)

#Obliczanie
print('Wyniki:\n')
print ('Czas lotu ciała wyniósł: ',round(czas,3),'[s]')
print ('Zasięg lotu wyniósł: ',round(zasieg,3),'[m]')
print ('Równanie toru ruchu ma postać: ',(wzory.rownanie(v,h)))

#Zapis do pliku
f = open("wyniki.txt", "a")
f.write('Oto program do symulacji ruchu poziomego z pewnej wysokośći H o danej prędkości początkowej V\n\n')
f.write('Użytkownik podał anstępujące dane:\n * Wysokość początkowa: '+str(h)+'\n * Prędkość początkowa: '+str(v)+'\n\n')
f.write('Otrzymane wyniki:\n')
f.write(' * Równanie toru ruchu ma postać: '+ str(rownanie) + '\n * Zasięg lotu wyniósł: ' + str(zasieg) + '[m]\n * Czas lotu ciała wyniósł: ' + str(czas) + '[s]')
f.close()

#Wykres
x=np.arange(0,int(zasieg + zasieg*0.05))
y= h - ((9.81 * (x**2)) / (2*(v**2)))
plt.plot(x,y, color='r', lw=1, ls='-', label='Tor ruchu ciała')
plt.ylim(0)
plt.legend()
plt.xlabel('Odległość', fontsize = 8)
plt.ylabel('Wysokość', fontsize = 8)
plt.savefig('wykres.jpg', dpi = 300)
plt.show()