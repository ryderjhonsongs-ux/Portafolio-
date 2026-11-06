#!/usr/init/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Matrices con Paso a Paso para Exámenes
Operaciones: Suma, Resta y Multiplicación por Escalar.
"""

def imprimir_matriz(matriz):
    """Muestra la matriz de forma limpia y ordenada."""
    for fila in matriz:
        print(" [ " + "  ".join(f"{val:8.2f}" for val in fila) + " ]")

def leer_matriz(nombre):
    """Permite ingresar una matriz por consola fila por fila."""
    print(f"\n--- Ingreso de la Matriz {nombre} ---")
    filas = int(input(f"Número de filas de {nombre}: "))
    cols = int(input(f"Número de columnas de {nombre}: "))
    
    matriz = []
    print("Ingrese los elementos fila por fila (separados por espacios):")
    for i in range(filas):
        while True:
            try:
                entrada = input(f"Fila {i+1}: ").strip().split()
                fila = [float(x) for x in entrada]
                if len(fila) != cols:
                    print(f"[Error] Debe ingresar exactamente {cols} elementos. Intente de nuevo.")
                    continue
                matriz.append(fila)
                break
            except ValueError:
                print("[Error] Ingrese solo números válidos.")
    return matriz

def sumar_matrices():
    print("\n=== SUMA DE MATRICES (A + B) ===")
    A = leer_matriz("A")
    B = leer_matriz("B")
    
    filas_a, cols_a = len(A), len(A[0])
    filas_b, cols_b = len(B), len(B[0])
    
    if filas_a != filas_b or cols_a != cols_b:
        print("\n[Error] Las dimensiones de las matrices no coinciden. No se puede sumar.")
        return

    print("\n" + "="*40)
    print("PROCEDIMIENTO PASO A PASO (PARA EL EXAMEN):")
    print("="*40)
    
    resultado = [[0.0 for _ in range(cols_a)] for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(cols_a):
            resultado[i][j] = A[i][j] + B[i][j]
            print(f"• Posición C_{i+1},{j+1} = A_{i+1},{j+1} + B_{i+1},{j+1}  -->  {A[i][j]} + {B[i][j]} = {resultado[i][j]}")

    print("\n" + "="*40)
    print("MATRIZ RESULTANTE FINAL:")
    print("="*40)
    imprimir_matriz(resultado)

def restar_matrices():
    print("\n=== RESTA DE MATRICES (A - B) ===")
    A = leer_matriz("A")
    B = leer_matriz("B")
    
    filas_a, cols_a = len(A), len(A[0])
    filas_b, cols_b = len(B), len(B[0])
    
    if filas_a != filas_b or cols_a != cols_b:
        print("\n[Error] Las dimensiones de las matrices no coinciden. No se puede restar.")
        return

    print("\n" + "="*40)
    print("PROCEDIMIENTO PASO A PASO (PARA EL EXAMEN):")
    print("="*40)
    
    resultado = [[0.0 for _ in range(cols_a)] for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(cols_a):
            resultado[i][j] = A[i][j] - B[i][j]
            print(f"• Posición C_{i+1},{j+1} = A_{i+1},{j+1} - B_{i+1},{j+1}  -->  {A[i][j]} - ({B[i][j]}) = {resultado[i][j]}")

    print("\n" + "="*40)
    print("MATRIZ RESULTANTE FINAL:")
    print("="*40)
    imprimir_matriz(resultado)

def escalar_matriz():
    print("\n=== MULTIPLICACIÓN POR ESCALAR (k * A) ===")
    k = float(input("Ingrese el valor del escalar (k): "))
    A = leer_matriz("A")
    
    filas, cols = len(A), len(A[0])

    print("\n" + "="*40)
    print("PROCEDIMIENTO PASO A PASO (PARA EL EXAMEN):")
    print("="*40)
    
    resultado = [[0.0 for _ in range(cols)] for _ in range(filas)]
    for i in range(filas):
        for j in range(cols):
            resultado[i][j] = k * A[i][j]
            print(f"• Posición C_{i+1},{j+1} = {k} * ({A[i][j]}) = {resultado[i][j]}")

    print("\n" + "="*40)
    print("MATRIZ RESULTANTE FINAL:")
    print("="*40)
    imprimir_matriz(resultado)

def main():
    while True:
        print("\n" + "="*40)
        print("   RESOLVEDOR DE MATRICES PARA EXAMEN")
        print("="*40)
        print("1. Suma de Matrices (A + B)")
        print("2. Resta de Matrices (A - B)")
        print("3. Multiplicación por Escalar (k * A)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            sumar_matrices()
        elif opcion == '2':
            restar_matrices()
        elif opcion == '3':
            escalar_matriz()
        elif opcion == '4':
            print("\n¡Saliendo! Mucho éxito en ese examen, a romperla.")
            break
        else:
            print("[Error] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
