#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Maestro 1: Toolkit de Distribución, Facturación y Normas Eléctricas
Autor: Samuel Enoc Gómez
Repositorio: Portafolio- (ryderjhonsongs-ux)
"""

import sys
import math

def mostrar_menu():
    print("\n" + "="*50)
    print("   TOOLKIT DE DISTRIBUCIÓN Y NORMATIVAS ELÉCTRICAS")
    print("="*50)
    print("1. Dimensionamiento de Conductores (Caída de Tensión)")
    print("2. Compensación de Factor de Potencia (Cálculo KVAR)")
    print("3. Ubicación Óptima de Transformadores (Centro de Cargas)")
    print("4. Análisis de Pérdidas No Técnicas (Fraude/Desviación)")
    print("5. Convertidor y Validador de Unidades Técnicas")
    print("6. Salir")
    print("="*50)

def dimensionar_conductores():
    print("\n--- [1] DIMENSIONAMIENTO DE CONDUCTORES ---")
    try:
        I = float(input("Ingrese la corriente de diseño (Amperios): "))
        L = float(input("Ingrese la longitud unidireccional del circuito (metros): "))
        V = float(input("Ingrese el voltaje nominal del sistema (Voltios): "))
        fp = float(input("Ingrese el factor de potencia (ej. 0.9): "))
        
        # Ejemplo simplificado de cálculo de sección por caída de tensión (Cobre: resistividad app 0.0175 ohm*mm2/m)
        # Caída de tensión máxima permitida típica: 3%
        caida_max_pct = 3.0
        v_caida_max = (V * caida_max_pct) / 100.0
        
        # Sección aproximada monofásica/trifásica orientativa
        # Usaremos fórmula estándar monofásica/trifásica simplificada para cobre
        seccion = (2 * 0.0175 * L * I) / v_caida_max
        
        print(f"\n[Resultado]")
        print(f"Sección teórica mínima calculada: {seccion:.2f} mm²")
        print("Nota: Verifique comercialmente con tablas de ampacidad y factores de corrección.")
    except ValueError:
        print("[Error] Ingrese valores numéricos válidos.")

def compensacion_fp():
    print("\n--- [2] COMPENSACIÓN DE FACTOR DE POTENCIA ---")
    try:
        P = float(input("Ingrese la potencia activa (kW): "))
        fp_actual = float(input("Ingrese el factor de potencia actual (ej. 0.75): "))
        fp_deseado = float(input("Ingrese el factor de potencia deseado (ej. 0.95): "))
        
        if not (0 < fp_actual < 1) or not (0 < fp_deseado <= 1):
            print("[Error] El factor de potencia debe estar entre 0 y 1.")
            return
            
        theta_actual = math.acos(fp_actual)
        theta_deseado = math.acos(fp_deseado)
        
        kvar = P * (math.tan(theta_actual) - math.tan(theta_deseado))
        
        print(f"\n[Resultado]")
        print(f"Potencia reactiva necesaria a instalar: {kvar:.2f} KVAR")
    except ValueError:
        print("[Error] Datos de entrada incorrectos.")

def ubicacion_transformadores():
    print("\n--- [3] UBICACIÓN ÓPTIMA DE TRANSFORMADORES (Centro de Cargas) ---")
    print("Ingrese las coordenadas (X, Y) y la carga (KVA) de los puntos de consumo:")
    n = int(input("Cantidad de nodos o cargas a evaluar: "))
    
    sum_x_s = 0
    sum_y_s = 0
    sum_s = 0
    
    for i in range(n):
        print(f"\n--- Nodo {i+1} ---")
        x = float(input(f"Coordenada X_{i+1}: "))
        y = float(input(f"Coordenada Y_{i+1}: "))
        s = float(input(f"Carga S_{i+1} (KVA): "))
        
        sum_x_s += x * s
        sum_y_s += y * s
        sum_s += s
        
    if sum_s == 0:
        print("[Error] La carga total no puede ser cero.")
        return
        
    x_optimo = sum_x_s / sum_s
    y_optimo = sum_y_s / sum_s
    
    print(f"\n[Resultado]")
    print(f"Coordenada óptima del transformador -> X: {x_optimo:.2f}, Y: {y_optimo:.2f}")

def perdidas_no_tecnicas():
    print("\n--- [4] ANÁLISIS DE PÉRDIDAS NO TÉCNICAS ---")
    try:
        energia_sub = float(input("Energía total inyectada al circuito/subestación (kWh): "))
        energia_fac = float(input("Energía total registrada por facturación de medidores (kWh): "))
        perdidas_tec_est = float(input("Porcentaje estimado de pérdidas técnicas regulatorias (ej. 5%): "))
        
        perdida_total = energia_sub - energia_fac
        perdida_total_pct = (perdida_total / energia_sub) * 100
        
        energia_no_tecnica = energia_sub * ((perdida_total_pct - perdidas_tec_est) / 100.0)
        if energia_no_tecnica < 0:
            energia_no_tecnica = 0
            
        print(f"\n[Resultado]")
        print(f"Pérdidas Totales en Red: {perdida_total:.2f} kWh ({perdida_total_pct:.2f}%)")
        print(f"Estimado de Pérdidas No Técnicas (Fraude/Anomalías): {energia_no_tecnica:.2f} kWh")
    except ValueError:
        print("[Error] Ingrese valores válidos.")

def convertidor_unidades():
    print("\n--- [5] CONVERTIDOR DE UNIDADES TÉCNICAS ---")
    print("1. HP a Kilovatios (kW)")
    print("2. AWG a Sección Aproximada (mm²)")
    op = input("Seleccione conversión: ")
    
    if op == '1':
        hp = float(input("Ingrese potencia en HP: "))
        kW = hp * 0.746
        print(f"Equivalente: {kW:.3f} kW")
    elif op == '2':
        # Tabla básica de referencia AWG a mm²
        tabla_awg = {
            "14": 2.08, "12": 3.31, "10": 5.26, "8": 8.37, 
            "6": 13.3, "4": 21.2, "2": 33.6, "1/0": 53.5
        }
        awg = input("Ingrese calibre AWG (ej. 12, 10, 8, 4): ")
        if awg in tabla_awg:
            print(f"Sección nominal aproximada: {tabla_awg[awg]} mm²")
        else:
            print("[Aviso] Calibre no encontrado en la tabla rápida base.")
    else:
        print("[Error] Opción no válida.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == '1':
            dimensionar_conductores()
        elif opcion == '2':
            compensacion_fp()
        elif opcion == '3':
            ubicacion_transformadores()
        elif opcion == '4':
            perdidas_no_tecnicas()
        elif opcion == '5':
            convertidor_unidades()
        elif opcion == '6':
            print("\nSaliendo del toolkit. ¡A descansar o seguir triunfando!")
            sys.exit(0)
        else:
            print("[Error] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
