import time

# der Abstand der aktuellen Zeitzone von der Null-Meridan-Zeitzone
print("altzone-Funktion: ", time.altzone)

# 'Pausieren' des Programms:
print("Vor der Pause")
time.sleep(2.4)
print("Nach der Pause")

# Zeitmessung
# weitere Hinweise: https://gertingold.github.io/pythonnawi/profiling.html
# weitere Möglichkeit: timeit einbinden http://jupiter-online.net/python-laufzeit-messen-mit-timeit/
# vgl. auch Sweigart
t1 = time.perf_counter()
for z in range(5):
    print(z)
    time.sleep(0.5)
t2 = time.perf_counter()
print(t2 - t1)

