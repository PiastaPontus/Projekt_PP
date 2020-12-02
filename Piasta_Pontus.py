#Modelowanie - projekt, Nikodem Piasta, Robert Pontus
#Modelownie rzutu poziomego w polu grawitacyjnym.

import numpy as np
import matplotlib.pyplot as plt

print ('Oto program do symulacji ruchu poziomego z pewnej wysokośći H o danej prędkości początkowej V')

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

#plik = np.loadtxt('plik.py')(tworzenie pliku ze wzorami 10.12.2020r.)
g=9.81 # to bedzie w pliku zew.
print('Dane: wysokość - h=',h,'[m]\n prędkość początkowa: v=',v, '[m/s]\n przyspieszenie ziemskie - g=',g,'[m/s^2]')

#def zasieg():
    #f-cje (10.12.2020r. - implementacja pliku ze wzorem)
#zasieg()

#def czas():
    #f-cje (10.12.2020r. - implementacja pliku ze wzorem)
#czas()

#def tor():
    #f-cje (10.12.2020r. - implementacja pliku ze wzorem)
#tor()

#print('Wyniki') 17.12.2020r.

#wykres (17.12.2020r.)
#plt.plot(x,y,color='r', lw=1, ls='-', label='wzorek')
#plt.legend()
#plt.xlabel('X', fontsize = 8)
#plt.ylabel('f(x)', fontsize = 8)
#plt.show()


#Zapis do pliku (17.12.2020r.)