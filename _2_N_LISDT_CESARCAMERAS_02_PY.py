### encabezado de librerias y variables globales
### fuiones secundarias
def funcion_secundario(numero):
    print(" el numero recibido :", numero)

def funcio_secundario_dos(numero_dos):
    print(" el numero dos recibido es:", numero_dos)
    resultado=numero_dos*numero_dos
    return resultado
### funcion principal 
def main():
    print("actividad 02- primer programa estruturado")
    variable=int(input("ingresa el valor a imprimir:\n"))
    funcion_secundario(variable)
    resultado_multiplicadocion=funcio_secundario_dos(variable)
    print(" el resultado de la multiplicaccion es :", resultado_multiplicadocion)
if __name__ == "__main__":
    main()
