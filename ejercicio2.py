sb= float(input("Ingrese el salario basico del vendedor: "))
v1= int(input("Ingrese el valor 1:"))
v2= int(input("Ingrese el valor 2:"))
v3= int(input("Ingrese el valor 3:"))
tot_vta= v1 + v2 + v3
com= tot_vta*0.10
tpag= sb + com
print(f"El total a pagar al vendedor es: {tpag}")
