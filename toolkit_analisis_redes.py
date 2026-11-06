#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Maestro 2: Toolkit de Análisis de Redes, Monitoreo y Activos
Autor: Samuel Enoc Gómez
Repositorio: Portafolio- (ryderjhonsongs-ux)
"""

import sys
import math
import time

def mostrar_menu():
    print("\n" + "="*50)
    print("   TOOLKIT DE ANÁLISIS DE REDES Y ACTIVOS ELÉCTRICOS")
    print("="*50)
    print("1. Flujo de Carga (Load Flow - Método Gauss-Seidel Simplificado)")
    print("2. Monitoreo y Alerta de Parámetros de Red (Simulación Serial/MQTT)")
    print("3. Analizador de Distorsión Armónica Total (THD)")
    print("4. Auditoría Energética y Análisis de Demanda")
    print("5. Gestor de Inventario y Mantenimiento de Transformadores")
    print("6. Salir")
    print("="*50)

def flujo_carga():
    print("\n--- [1] FLUJO DE CARGA (GAUSS-SEIDEL SIMPLIFICADO) ---")
    print("Evaluación iterativa de tensiones en un nodo de carga simple.")
    try:
        V_nominal = float(input("Voltaje base del sistema (V): "))
        P_req = float(input("Potencia activa demandada (MW): "))
        Q_req = float(input("Potencia reactiva demandada (MVAR): "))
        R_linea = float(input("Resistencia de la línea (Ohm): "))
        X_linea = float(input("Reactancia de la línea (Ohm): "))
        
        # Estimación iterativa simplificada de caída y voltaje nodal
        V_iter = V_nominal
        tolerancia = 0.001
        max_iter = 50
        
        for i in range(max_iter):
            # Corriente aproximada I = S* / V*
            I_mag = math.sqrt(P_req**2 + Q_req**2) * 1e6 / V_iter
            # Caída de voltaje aproximada Delta V = I * (R*cos(theta) + X*sin(theta)) -> Simplificada por impedancia
            caida = I_mag * math.sqrt(R_linea**2 + X_linea**2)
            V_nuevo = V_nominal - caida
            
            if abs(V_nuevo - V_iter) < tolerancia:
                V_iter = V_nuevo
                break
            V_iter = V_nuevo
            
        print(f"\n[Resultado Convergencia]")
        print(f"Voltaje nodal estimado al final de la línea: {V_iter:.2f} V")
        print(f"Desviación porcentual respecto a base: {((V_nominal - V_iter)/V_nominal)*100:.2f}%")
    except ValueError:
        print("[Error] Ingrese parámetros numéricos válidos.")

def monitoreo_red():
    print("\n--- [2] MONITOREO Y ALERTA DE PARÁMETROS DE RED ---")
    print("Simulando lectura de tramas de datos en tiempo real (Puerto Serial / MQTT)...")
    print("Presione Ctrl+C para detener la simulación de monitoreo.\n")
    try:
        for _ in range(5):
            # Simulando fluctuaciones aleatorias de voltaje y desbalance
            import random
            volt_fase_a = round(random.uniform(110.0, 132.0), 2)
            volt_fase_b = round(random.uniform(110.0, 129.0), 2)
            volt_fase_c = round(random.uniform(105.0, 128.0), 2)
            
            print(f"[DATA RECIBIDA] Fase A: {volt_fase_a}V | Fase B: {volt_fase_b}V | Fase C: {volt_fase_c}V")
            
            # Alertas críticas
            if volt_fase_a > 130 or volt_fase_b > 130 or volt_fase_c > 130:
                print("   ⚠️ ¡ALERTA CRÍTICA: Sobreitensión detectada en línea!")
            elif volt_fase_a < 108 or volt_fase_b < 108 or volt_fase_c < 108:
                print("   ⚠️ ¡ALERTA CRÍTICA: Subtensión o caída severa detectada!")
            else:
                print("   Estado: Parámetros dentro de rango nominal seguro.")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoreo pausado por el usuario.")

def analizador_thd():
    print("\n--- [3] ANALIZADOR DE DISTORSIÓN ARMÓNICA TOTAL (THD) ---")
    try:
        print("Ingrese los valores RMS de las componentes armónicas principales:")
        I1 = float(input("Corriente fundamental (I1 - Amperios): "))
        I3 = float(input("Corriente de 3er armónico (I3): "))
        I5 = float(input("Corriente de 5to armónico (I5): "))
        I7 = float(input("Corriente de 7mo armónico (I7): "))
        
        # Fórmula de THD = (Raíz cuadrada de la suma de cuadrados de armónicos) / Fundamental * 100
        suma_cuadrados = (I3**2) + (I5**2) + (I7**2)
        thd = (math.sqrt(suma_cuadrados) / I1) * 100.0
        
        print(f"\n[Resultado]")
        print(f"Distorsión Armónica Total (THD-i): {thd:.2f}%")
        if thd > 8.0:
            print("Recomendación: THD elevado. Se sugiere instalar filtros armónicos pasivos o activos.")
        else:
            print("THD dentro de límites aceptables según IEEE 519.")
    except ValueError:
        print("[Error] Ingrese datos numéricos válidos.")

def auditoria_energetica():
    print("\n--- [4] AUDITORÍA ENERGÉTICA Y CURVAS DE CARGA ---")
    try:
        p_pico = float(input("Ingrese la demanda máxima registrada (kW): "))
        consumo_mensual = float(input("Ingrese el consumo total mensual (kWh): "))
        horas_mes = float(input("Total de horas operativas en el mes (ej. 720 h): "))
        
        demanda_media = consumo_mensual / horas_mes
        factor_carga = (demanda_media / p_pico) * 100.0 if p_pico > 0 else 0
        
        print(f"\n[Resultado de Auditoría]")
        print(f"Demanda Media del periodo: {demanda_media:.2f} kW")
        print(f"Factor de Carga de la instalación: {factor_carga:.2f}%")
        if factor_carga < 50:
            print("Diagnóstico: Factor de carga bajo. La instalación desaprovecha la capacidad instalada; evaluar gestión de picos.")
        else:
            print("Diagnóstico: Factor de carga saludable y eficiente.")
    except ValueError:
        print("[Error] Ingrese valores numéricos correctos.")

def gestor_transformadores():
    print("\n--- [5] GESTOR DE INVENTARIO Y MANTENIMIENTO DE TRANSFORMADORES ---")
    print("Registro rápido de estado operativo de equipos de potencia.")
    
    id_trafo = input("Identificador o Código del Transformador (ej. TR-04): ")
    kva = input("Capacidad nominal (KVA): ")
    temp_aceite = float(input("Última temperatura de aceite registrada (°C): "))
    rigidez_dielectrica = float(input("Resultado de prueba de rigidez dieléctrica del aceite (kV): "))
    
    print(f"\n[Ficha Técnica y Diagnóstico: {id_trafo}]")
    print(f"Capacidad: {kva} KVA")
    
    alerta_mant = []
    if temp_aceite > 85.0:
        alerta_mant.append("Temperatura de aceite crítica (>85°C). Revisar sobrecarga o ventilación.")
    if rigidez_dielectrica < 30.0:
        alerta_mant.append("Rigidez dieléctrica baja (<30 kV). Urgente tratamiento o filtrado de aceite.")
        
    if alerta_mant:
        print("Estado: REQUIERE MANTENIMIENTO PREVENTIVO.")
        for alerta in alerta_mant:
            print(f" - {alerta}")
    else:
        print("Estado: Operativo en óptimas condiciones.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == '1':
            flujo_carga()
        elif opcion == '2':
            monitoreo_red()
        elif opcion == '3':
            analizador_thd()
        elif opcion == '4':
            auditoria_energetica()
        elif opcion == '5':
            gestor_transformadores()
        elif opcion == '6':
            print("\nSaliendo del toolkit de análisis. ¡Descansa o sigue avanzando con fuerza!")
            sys.exit(0)
        else:
            print("[Error] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
