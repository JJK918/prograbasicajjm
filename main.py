from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada
from es.salida import producir_archivo

if __name__ == "__main__":
    print(f"{"*" * 6} MENU {"*" * 6}")

    historial = []

    while True:
        opcion = recibir_opcion("Introduce una opción: ", operaciones)

        a = recibir_entrada("Introduce un numero: ")

        b = recibir_entrada("Introduce otro numero: ")

        resultado = operaciones[opcion](a, b)

        historial.append({
            "Operacion": opcion,
            "A": a,
            "B": b
        })

        producir_archivo("historial.csv", historial)

        print(f"#=> {resultado}")
        print("El programa continua")