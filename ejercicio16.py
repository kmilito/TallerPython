exmate=float(input("Digite la nota del examen de matemáticas: "))
tareamat1= float(input("Digite la nota de la primera tarea de matemáticas: "))
tareamat2= float(input("Digite la nota de la segunda tarea de matemáticas: "))
tareamat3= float(input("Digite la nota de la tercera tarea de matemáticas: "))
mat= 0.90*exmate+ 0.10*(tareamat1 + tareamat2 + tareamat3)/3
print(f"El promedio de la materia de matemáticas es: {mat}")

exfis= float(input("Digite la nota del examen de Fisica: "))
tareafis1= float(input("Digite la nota de la primera tarea de Fisica: "))
tareafis2= float(input("Digite la nota de la segunda tarea de Fisica: "))

fis= 0.80*exfis+ 0.20*(tareafis1 + tareafis2)/2
print(f"El promedio de la materia de Fisica es: {fis}")

exquim= float(input("Digite la nota del examen de Quimica: "))
tareaquim1= float(input("Digite la nota de la primera tarea de Quimica: "))
tareaquim2= float(input("Digite la nota de la segunda tarea de Quimica: "))
tareaquim3= float(input("Digite la nota de la tercera tarea de Quimica: "))

quim= 0.85*exquim+ 0.15*(tareaquim1 + tareaquim2 +tareaquim3)/3
print(f"El promedio de la materia de Quimica es: {quim}")

asign= (mat + fis + quim)/3
print(f"El promedio de las tres asignaturas es: {asign}")


