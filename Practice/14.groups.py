name = input('Hola,¿Cual es tu nombre?')
gender = input("¿Cuál es tu sexo (M o F)? ")
if gender == "F":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
