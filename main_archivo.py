from aritmetica import operaciones, division, multiplicacion, resta, suma
from es.entrada import recibir_opcion, recibir_entrada, validar_entrada, validar_opcion, recibir_ruta, procesar_archivo

if __name__ == "__main__":
    print(f"{"*" * 6} MENU {"*" * 6}")

    ruta = recibir_ruta("Introduce la dirección de un archivo: ")

    for fila in procesar_archivo(ruta):
        opcion = validar_opcion(fila["Operacion"], operaciones)
        a = validar_entrada(fila["A"])
        b = validar_entrada(fila["B"])

        resultado = operaciones[opcion](a, b)

        print(f"#=> {resultado}")
        print("El programa continua")