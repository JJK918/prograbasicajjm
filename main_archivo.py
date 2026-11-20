from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada, validar_entrada, validar_opcion, recibir_ruta, procesar_archivo

if __name__ == "__main__":
    print(f"{'*' * 6} MENU {'*' * 6}")

    while True:
        try:
            ruta = recibir_ruta("Introduce la dirección de un archivo: ")
            filas = list(procesar_archivo(ruta))
        except FileNotFoundError:
            print("Error: no se encontró el archivo en la ruta indicada. Inténtalo de nuevo.")
        else:
            break

    for fila in filas:
        try:
            opcion = validar_opcion(fila["Operacion"], operaciones)
            a = validar_entrada(fila["A"])
            b = validar_entrada(fila["B"])

            resultado = operaciones[opcion](a, b)
        except ValueError:
            print(f"Error de valor: los datos '{fila.get('A')}' o '{fila.get('B')}' no se pueden convertir a número.")
        except KeyError:
            print(f"La opción '{fila.get('Operacion')}' no es válida. Las opciones disponibles son: {', '.join(operaciones.keys())}.")
        except ZeroDivisionError:
            print("No se puede ejecutar la operación de división con un denominador 0.")
        except (TypeError, NameError):
            print("Ocurrió un error inesperado de tipo o nombre. Vuelve a intentarlo.")
        else:
            print(f"#=> {resultado}")
        finally:
            print("El programa continúa")