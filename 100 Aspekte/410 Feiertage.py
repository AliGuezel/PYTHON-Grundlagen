#
# Neben den unbeweglichen Feiertagen, gibt es eine ganze Reihe
# beweglicher Feiertage, die sich allesamt am Ostersonntag eines
# Jahres ausrichten.
# Christie Himmelfahrt z.B. ist 39 Tage nach Ostersonntag
#
# Will man die Feiertage ausrechnen, muß man also zunächst das
# Datum für Ostersonntag errechnen:
# https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel
#
# Zu beachten ist dann noch, daß nicht alle Feiertage bundesweit
# gelten, der Augsburger Religionsfriede gilt sogar nur dort!
#
# Für Comcave allerdings ist jeder Feiertag ein Feiertag!!!
#
# nachfolgender Code wurde aus eine C#-Implementierung übernommen
# er ist also nicht besonders 'Pythonesk'
# zu beachten ist, daß alle Divisionen als Ganzzahl-Divisionen
# umgesetzt werden
#

import datetime

def OsterSonntag(Jahr):

    if Jahr < 1583 or Jahr > 4099:
        raise Exception()

    firstDigits = 0
    remaining19 = 0
    temp = 0
    tA = 0
    tB = 0
    tC = 0
    tD = 0
    tE = 0

    firstDigits = Jahr // 100
    remaining19 = Jahr % 19

    AbzugMinusEins = (21, 24, 25, 27, 28, 29, 30, 31, 32, 34, 35, 38)
    AbzugMinusZwei = (33, 36, 37, 39, 40)

    temp = (firstDigits - 15) // 2 + 202 - 11 * remaining19

    if firstDigits in AbzugMinusEins:
        temp -= 1
    if firstDigits in AbzugMinusZwei:
        temp -= 2

    temp = temp % 30

    tA = temp + 21
    if temp == 29:
        tA = tA - 1
    if temp == 28 and remaining19 > 10:
        tA = tA - 1

    tB = (tA - 19) % 7

    tC = (40 - firstDigits) % 4
    if tC == 3:
        tC = tC + 1
    if tC > 1:
        tC = tC + 1

    temp = Jahr % 100
    tD = (temp + temp // 4) % 7

    tE = ((20 - tB - tC - tD) % 7) + 1

    day = tA + tE
    month = 0

    if day > 31:
        day -= 31
        month = 4
    else:
        month = 3

    return datetime.datetime(Jahr, int(month), int(day))

print("Tests:")
for jahr in range(2010, 2026):
    print(OsterSonntag(jahr))


# Alternative
from dateutil import easter
for jahr in range(2010, 2026):
    print(easter.easter(jahr))