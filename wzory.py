import math

g = 9.81
zasieg = lambda v, h: v * math.sqrt(2 * h / g)
czas = lambda h: math.sqrt(2 * h / g)
rownanie = lambda h, v: str("y(x) = " + str(h) + " - (" + str(g) + "/2)/(" + str(v) + "**2) * x^2")
