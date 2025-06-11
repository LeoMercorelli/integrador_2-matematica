# ==========================================
# FUNCIONES AUXILIARES DEL PROGRAMA
# ==========================================

# Funcion que determina si un anio es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Funcion que convierte un DNI en un conjunto de digitos unicos
def obtener_digitos_unicos(dni):
    return set(str(dni))

# Funcion que cuenta cuantas veces aparece cada digito (0 al 9) en cada DNI dado
def frecuencia_digitos(dni):
    freq = {}
    for i in range(10):
        i_str = str(i)
        freq[i_str] = dni.count(i_str)
    return freq

# Funcion que suma todos los digitos de un DNI, incluyendo repeticiones
def suma_digitos(dni):
    return sum(int(d) for d in str(dni))

# Funcion que genera el producto cartesiano entre dos listas (anios y edades)
def producto_cartesiano(set1, set2):
    return [(a, b) for a in set1 for b in set2]

# Funcion que compara dos conjuntos y muestra si son equivalentes, equilibrados o dispares
def comparar_conjuntos(nombre1, c1, nombre2, c2):
    suma1 = sum(int(d) for d in c1)
    suma2 = sum(int(d) for d in c2)

    print(f"\nComparacion entre {nombre1} y {nombre2}")
    print(f"Digitos unicos de {nombre1}: {sorted(c1)} -> Suma: {suma1}")
    print(f"Digitos unicos de {nombre2}: {sorted(c2)} -> Suma: {suma2}")

    if len(c1) == len(c2) and suma1 == suma2:
        print("Resultado: Conjuntos equilibrados y equivalentes")
    elif len(c1) == len(c2):
        print("Resultado: Conjuntos equilibrados")
    elif suma1 == suma2:
        print("Resultado: Conjuntos equivalentes")
    else:
        print("Resultado: Conjuntos dispares")

# Funcion que pregunta si el usuario quiere avanzar con la siguiente seccion o reiniciar todo
def esperar_confirmacion(seccion):
    while True:
        opcion = input(f"\n¿Desea continuar con la seccion {seccion}? (s/n): ").lower()
        if opcion == 's':
            return True
        elif opcion == 'n':
            return False
        else:
            print("Opcion invalida. Ingrese 's' para continuar o 'n' para reiniciar.")

# Funcion principal que ejecuta todo el programa paso a paso
def main():
    while True:
        print("\n==========================================")
        print("SECCION 1: INGRESO DE DATOS")
        print("==========================================")

        n_integrantes = int(input("Ingrese la cantidad de integrantes del grupo: "))
        datos = {}

        for i in range(n_integrantes):
            nombre = input(f"\nIngrese el nombre de la persona {i+1}: ")
            while True:
                dni = input(f"Ingrese el DNI de {nombre} (sin puntos ni espacios): ")
                if dni.isdigit() and len(dni) >= 7:
                    break
                else:
                    print("DNI invalido. Ingrese solo numeros, sin puntos ni letras.")
            anio = int(input(f"Ingrese el anio de nacimiento de {nombre} (formato 4 digitos): "))
            datos[nombre] = {"dni": dni, "anio": anio}

        if not esperar_confirmacion(2):
            continue

        print("\n==========================================")
        print("SECCION 2: CONJUNTOS DE DIGITOS UNICOS")
        print("==========================================")

        conjuntos_unicos = {}
        for nombre, info in datos.items():
            conjuntos_unicos[nombre] = obtener_digitos_unicos(info["dni"])

        for nombre, conjunto in conjuntos_unicos.items():
            print(f"{nombre}: {sorted(conjunto)}")

        if not esperar_confirmacion(3):
            continue

        print("\n==========================================")
        print("SECCION 3: OPERACIONES ENTRE CONJUNTOS")
        print("==========================================")

        nombres = list(conjuntos_unicos.keys())
        for i in range(len(nombres)):
            for j in range(i + 1, len(nombres)):
                A = conjuntos_unicos[nombres[i]]
                B = conjuntos_unicos[nombres[j]]
                print(f"\nEntre {nombres[i]} y {nombres[j]}:")
                print(f"- Union: {sorted(A | B)}")
                print(f"- Interseccion: {sorted(A & B)}")
                print(f"- Diferencia {nombres[i]} - {nombres[j]}: {sorted(A - B)}")
                print(f"- Diferencia {nombres[j]} - {nombres[i]}: {sorted(B - A)}")
                print(f"- Diferencia simetrica: {sorted(A ^ B)}")

        if not esperar_confirmacion(4):
            continue

        print("\n==========================================")
        print("SECCION 4: FRECUENCIA Y SUMA DE DIGITOS POR DNI")
        print("==========================================")

        for nombre, info in datos.items():
            print(f"\n{nombre}:")
            print(f"- Frecuencia: {frecuencia_digitos(info['dni'])}")
            print(f"- Suma de digitos: {suma_digitos(info['dni'])}")

        if not esperar_confirmacion(5):
            continue

        print("\n==========================================")
        print("SECCION 5: EXPRESION 1 - DIGITOS COMUNES")
        print("==========================================")

        for i in range(len(nombres)):
            for j in range(i + 1, len(nombres)):
                A = conjuntos_unicos[nombres[i]]
                B = conjuntos_unicos[nombres[j]]
                interseccion = A & B
                if interseccion:
                    print(f"{nombres[i]} y {nombres[j]} tienen en comun: {sorted(interseccion)}")
                else:
                    print(f"{nombres[i]} y {nombres[j]} no tienen digitos en comun")

        if not esperar_confirmacion(6):
            continue

        print("\n==========================================")
        print("SECCION 6: EXPRESION 2 - PARIDAD DE CONJUNTOS")
        print("==========================================")

        conjuntos_par = 0
        conjuntos_impar = 0
        mayorias = {}
        tipos = {}

        for nombre, digitos in conjuntos_unicos.items():
            cant_pares = sum(1 for d in digitos if int(d) % 2 == 0)
            cant_impares = len(digitos) - cant_pares

            if cant_pares > cant_impares:
                conjuntos_par += 1
                tipo = "par"
                mayor = cant_pares
            elif cant_impares > cant_pares:
                conjuntos_impar += 1
                tipo = "impar"
                mayor = cant_impares
            else:
                tipo = "equilibrado"
                mayor = cant_pares

            tipos[nombre] = tipo
            mayorias[nombre] = mayor

            print(f"{nombre}: {cant_impares} impares, {cant_pares} pares -> grupo {tipo}")

        print(f"\nTotal de conjuntos par: {conjuntos_par}")
        print(f"Total de conjuntos impar: {conjuntos_impar}")

        if len(nombres) >= 2:
            a, b = nombres[0], nombres[1]
            if mayorias[a] > mayorias[b]:
                print(f"\nComparacion especifica entre {a} y {b}: {a} tiene mas digitos dominantes. Grupo {tipos[a]}")
            elif mayorias[b] > mayorias[a]:
                print(f"\nComparacion especifica entre {a} y {b}: {b} tiene mas digitos dominantes. Grupo {tipos[b]}")
            else:
                print(f"\nComparacion especifica entre {a} y {b}: misma cantidad de digitos dominantes. Grupo equilibrado")

        if not esperar_confirmacion(7):
            continue

        print("\n==========================================")
        print("SECCION 7: EXPRESION 3 - COMPARACION ENTRE CONJUNTOS")
        print("==========================================")

        for i in range(len(nombres)):
            for j in range(i + 1, len(nombres)):
                comparar_conjuntos(nombres[i], conjuntos_unicos[nombres[i]], nombres[j], conjuntos_unicos[nombres[j]])

        if not esperar_confirmacion(8):
            continue

        print("\n==========================================")
        print("SECCION 8: ANALISIS DE ANIOS DE NACIMIENTO")
        print("==========================================")

        anios = [info["anio"] for info in datos.values()]
        pares = [a for a in anios if a % 2 == 0]
        impares = [a for a in anios if a % 2 != 0]

        print(f"Anios de nacimiento: {anios}")
        print(f"Cantidad de anios pares: {len(pares)}")
        print(f"Cantidad de anios impares: {len(impares)}")

        if all(a > 2000 for a in anios):
            print("Todos nacieron despues del 2000")
        else:
            print("No todos nacieron despues del 2000")

        if any(es_bisiesto(a) for a in anios):
            print("Al menos un integrante nacio en un anio bisiesto")
        else:
            print("Ningun integrante nacio en anio bisiesto")

        edades = [2025 - a for a in anios]
        producto = producto_cartesiano(anios, edades)
        print(f"Producto cartesiano entre anios y edades: {producto}")

        # Preguntar si desea repetir el programa
        print("\n==========================================")
        print("FIN DEL PROGRAMA")
        print("==========================================")
        repetir = input("¿Desea ejecutar el programa nuevamente? (s/n): ").lower()
        if repetir == 's':
            continue
        else:
            print("\nGracias por utilizar el programa. Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()
