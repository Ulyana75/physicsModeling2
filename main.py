"""
Первоначальная консольная программа
"""

from math import log

INCORRECT_DATA_MESSAGE = "Incorrect data!"
POACHERS_ARE_GUILTY = "Poachers are guilty!"
HUNTSMEN_ARE_KILLERS = "Huntsmen are killers!"

x1 = 31   # температура во время задержания
x2 = 29   # температура через час после задержания
x = 31   # температура, до которой ищем время
x0 = 37   # начальная температура (в момент выстрела)
a = 21   # температура окружающей среды

wt = 1.5

if (a > x0 and (x1 > x2 or x1 < x0)) or (a < x0 and (x1 < x2 or x1 > x0)) or (a == x0 and x1 != x2 != x0):
    print(INCORRECT_DATA_MESSAGE)
    exit(0)

t = log(abs(x0 - a) / abs(x - a)) / log(abs(x1 - a) / abs(x2 - a))
h = int(t)
m = 60 * (t - int(t))
print(h, m)

if t <= wt:
    print(HUNTSMEN_ARE_KILLERS)
else:
    print(POACHERS_ARE_GUILTY)
