import datetime

# Datumswerte können auch mit den üblichen Operatoren verglichen werden
print(datetime.date(2020, 5, 1) > datetime.date(2020, 4, 23))
print(datetime.datetime(2020, 5, 1, 12, 0, 0) > datetime.datetime(2020, 5, 1, 12, 5, 5))
print(datetime.time(12, 5, 5) > datetime.time(12, 0, 0))
