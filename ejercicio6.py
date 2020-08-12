from datetime import date
def calcular_edad(fecha_nac):
    diferencia_fechas = date.today() -fecha_nac
    diferencia_fechas_dias = diferencia_fechas.days
    edad_numerica = diferencia_fechas_dias / 365.2425
    edad = int(edad_numerica)
    return edad

fecha_nac = date(1991, 5, 18)
print(calcular_edad(fecha_nac))