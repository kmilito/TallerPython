edad=int(input("Ingrese su edad: "))
sexo=input("Ingrese si su sexo es Masculino o Femenino (M o F): ")

if sexo == 'F':
    npulsos= (220-edad)/10
    print(f"El numero de pulsaciones es: {npulsos}")
else:
    npulsos= (210-edad)/10
    print(f"El numero de pulsaciones que ud tiene es: {npulsos}")

