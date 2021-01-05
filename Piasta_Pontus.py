# Modelowanie - projekt, Nikodem Piasta, Robert Pontus
# Modelownie rzutu poziomego w polu grawitacyjnym.

import numpy as np
from tkinter import *
import wzory
from matplotlib import pyplot as plt

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

print('Dane:\n wysokość - h=', h, '[m]\n prędkość początkowa: v=', v, '[m/s]\n przyspieszenie ziemskie - g=', (wzory.g),
      '[m/s^2]\n\n')

#Zmienne
czas = wzory.czas(h)
zasieg = wzory.zasieg(v, h)
rownanie = wzory.rownanie(v, h)

#Obliczanie
print('Wyniki:\n')
print('Czas lotu ciała wyniósł: ', round(czas, 3), '[s]')
print('Zasięg lotu wyniósł: ', round(zasieg, 3), '[m]')
print('Równanie toru ruchu ma postać: ', (wzory.rownanie(v, h)))


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


#Animacja
x = np.linspace(float(0), float(zasieg + zasieg * 0.05), num=500)
y = h - ((9.81 * (x ** 2)) / (2 * (v ** 2)))

aspect = zasieg / h

new_h = 700
new_w = int(700*aspect)
print(new_w)
normal_x = []
normal_y = []

for val in x:
    normal_x.append(new_w* (val - 0 )/ (x[len(x)-1]))

for val in y:
    normal_y.append(new_h* (val - y[len(y)-1])/ ( y[0] - y[len(y)-1]))


root = Tk()
root.title("Animacja")
root.configure(width=int(700 * aspect) + 100, height=770)
canvas = Canvas(root, width=int(700 * aspect) + 40, height=740,bg='grey')
canvas.place(x=20, y=20)
X = normal_x[0]
Y = normal_y[0]
ball = canvas.create_oval(X - 20+100, Y + 20, X + 20+100, Y - 20, fill="red")
for i in range(len(normal_x) - 1):
    canvas.create_line(normal_x[i], 700 - normal_y[i], normal_x[i + 1], 700 - normal_y[i + 1])

i = 1
def move():
    global i
    canvas.coords(ball, normal_x[i], 700 - normal_y[i], normal_x[i]+40, 700 - normal_y[i] + 40)
    i += 1
    pass

def clock():
    move()
    if(i<len(x)):
        root.after(20, clock)
clock()


root.mainloop()