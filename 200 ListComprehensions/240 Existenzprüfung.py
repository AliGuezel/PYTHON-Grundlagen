#*****************************************************************
# Die Unternehmen sollen ermittelt werden, die Mitarbeiter aufweisen,
# denen nicht der Mindestlohn gezahlt wird
companies = {
                'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
                'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
                'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}
            }

# schleifenbasierte Lösung
erg = []
for Unternehmen in companies.items():
    AlleMitarbeiter = Unternehmen[1]
    for EinzelMitarbeiter in AlleMitarbeiter.items():
        if EinzelMitarbeiter[1] < 9 and Unternehmen[0] not in erg:
            erg.append(Unternehmen[0])
print(erg)

# mit Listenabstraktion
illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
print(illegal)