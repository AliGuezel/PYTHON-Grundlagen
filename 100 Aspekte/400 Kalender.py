# https://docs.python.org/3/library/calendar.html#module-calendar

import calendar
import locale

kalenderblatt = calendar.TextCalendar(calendar.MONDAY)
ausgabe = kalenderblatt.formatmonth(2020,1)
print(ausgabe)

for x in calendar.Calendar(firstweekday=1).iterweekdays():
    print(x)

print(list(calendar.day_name))

locale.setlocale(locale.LC_ALL, "de-DE")

print(list(calendar.day_name))

print(list(calendar.day_abbr))
print(list(calendar.month_name))
print(list(calendar.month_abbr))

print("Erster Tag der Woche ist Montag:", calendar.firstweekday() == calendar.MONDAY)

print("ist 2020 ein Schaltjahr:", calendar.isleap(2020))
print("Schaltjahre zwischen 1900 und 1920:", calendar.leapdays(1900, 1921))

print("Tag vom 12.3.2020:", calendar.weekday(2020, 3, 12))

# ergibt erster Tag des Monats und die Anzahl der Tage
print(calendar.monthrange(2020, 4))

