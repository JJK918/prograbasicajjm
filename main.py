from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada
from es.salida import producir_archivo

if __name__ == "__main__":
    print(f"{'*' * 6} MENU {'*' * 6}")

    historial = []

    while True:
        while True:
            try:
                opcion = recibir_opcion("Introduce una opción: ", operaciones)
            except KeyError:
                print(f"La opción que ingresó no es válida. Las opciones disponibles son: {', '.join(operaciones.keys())}.")
            else:
                break

        while True:
            try:
                a = recibir_entrada("Introduce un número: ")
            except ValueError:
                print("Error: el dato ingresado no se puede convertir a número. Inténtalo de nuevo.")
            else:
                break

        while True:
            try:
                b = recibir_entrada("Introduce otro número: ")
            except ValueError:
                print("Error: el dato ingresado no se puede convertir a número. Inténtalo de nuevo.")
            else:
                break

        try:
            resultado = operaciones[opcion](a, b)

            historial.append({
                "Operacion": opcion,
                "A": a,
                "B": b
            })

            producir_archivo("historial.csv", historial)
        except KeyError:
            print(f"La opción que ingresó no es válida. Las opciones disponibles son: {', '.join(operaciones.keys())}.")
        except ZeroDivisionError:
            print("No se puede ejecutar la operación de división con un denominador 0.")
        except (TypeError, NameError):
            print("Ocurrió un error inesperado de tipo o nombre. Vuelve a intentarlo.")
        else:
            print(f"#=> {resultado}")
        finally:
            print("El programa continúa")