cal1= float(input("Digite la calificacion 1 del estudiante: "))
cal2= float(input("Digite la calificacion 2 del estudiante: "))
cal3= float(input("Digite la calificacion 3 del estudiante: "))
exf= float(input("Digite la calificacion del examen final: "))
tfinal= float(input("Digite la calificacion del trabajo final: "))
prom= (cal1 + cal2 + cal3)/3
ppar= prom * 0.55
promef= exf*0.30
promtfinal= tfinal * 0.15
calfin= ppar + promef + promtfinal
print(f"La calificacion final del estudiante es: {calfin: .2f}")

