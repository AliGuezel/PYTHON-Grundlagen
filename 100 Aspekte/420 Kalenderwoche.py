# https://www.spektrum.de/raetsel/die-54-kalenderwoche/1659570
# https://de.wikipedia.org/wiki/Woche#Kalenderwoche

import datetime
import locale

locale.setlocale(locale.LC_ALL, "de-DE")

print(datetime.date.today().isocalendar())
print(datetime.date(2022,1,1).isocalendar()[1])
print(datetime.date(2022,1,3).isocalendar()[1])
print(datetime.date(2022,12,31).isocalendar()[1])


