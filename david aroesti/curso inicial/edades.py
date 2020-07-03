
name_1 = input("¿Cual es tu nombre?: ");
age_1 = int(input("¿cual es su edad? " ));

name_2 = input("¿cual es tu nombre?: ");
age_2 = int(input("¿cual es su edad? "));

if age_1 > age_2:
  print(f" {name_1} es mayor que {name_2}");
elif age_1 < age_2:
  print(f"{name_1} es menor que {name_2}")
elif age_1 > 62 and age_2 >58:
   print(f"{name_1} y {name_2} son cuchos")
else:
  print(f"{name_1} y {name_2} tienen igual edad")

