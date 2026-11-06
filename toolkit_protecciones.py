#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Maestro 3: Toolkit de Protecciones, Instalaciones y Diseño Físico
Autor: Samuel Enoc Gómez
Repositorio: Portafolio- (ryderjhonsongs-ux)
"""

import sys
import math

def mostrar_menu():
    print("\n" + "="*50)
    print("   TOOLKIT DE PROTECCIONES, INSTALACIONES Y DISEÑO")
    print("="*50)
    print("1. Simulador de Corriente de Cortocircuito Trifásico/Monofásico")
    print("2. Generador de Presupuestos y Lista de Materiales (BOM)")
    print("3. Diseño y Verificación de Mallas de Puesta a Tierra (IEEE 80)")
    print("4. Coordinación de Protecciones de Sobrecorriente")
    print("5. Cálculo de Iluminación (Método de los Lúmenes)")
    print("6. Salir")
    print("="*50)

def simulador_cortocircuito():
    print("\n--- [1] SIMULADOR DE CORTO CIRCUITO ---")
    try:
        V_ll = float(input("Voltaje nominal línea a línea (V): "))
        MVA_cc = float(input("Potencia de cortocircuito en el nodo o MVA de corto del transformador: "))
        Z_tf_pct = float(input("Impedancia porcentual del transformador (Z% ej. 5.7%): "))
        
        # Corriente de cortocircuito trifásica simétrica aproximada (Icc = S_cc / (sqrt(3) * V_ll))
        # O estimada mediante impedancia base
        if MVA_cc > 0:
            Icc_kA = (MVA_cc * 1e3) / (math.sqrt(3) * V_ll)
            print(f"\n[Resultado]")
            print(f"Corriente de Cortocircuito Trifásica estimada: {Icc_kA:.2f} kA")
            print(f"Capacidad interruptora mínima recomendada para protecciones: {math.ceil(Icc_kA * 1.25)} kA")
        else:
            print("[Error] La potencia de cortocircuito debe ser mayor a cero.")
    except ValueError:
        print("[Error] Ingrese valores numéricos válidos.")

def generador_presupuestos_bom():
    print("\n--- [2] GENERADOR DE PRESUPUESTOS Y LISTA DE MATERIALES (BOM) ---")
    try:
        puntos_luz = int(input("Cantidad de puntos de iluminación/salidas: "))
        tomas = int(input("Cantidad de tomacorrientes dobles: "))
        metros_tubo = float(input("Metros estimados de tubería EMT/PVC: "))
        
        # Costos unitarios de referencia simulados
        costo_punto_luz = 15.0
        costo_toma = 12.0
        costo_metro_tubo = 3.5
        costo_cable_m = 1.8
        
        total_cable = metros_tubo * 3  # Fase, neutro, tierra
        
        subtotal_luz = puntos_luz * costo_punto_luz
        subtotal_tomas = tomas * costo_toma
        subtotal_tuberia = metros_tubo * costo_metro_tubo
        subtotal_cable = total_cable * costo_cable_m
        
        total_general = subtotal_luz + subtotal_tomas + subtotal_tuberia + subtotal_cable
        
        print("\n" + "-"*40)
        print("          LISTA DE MATERIALES (BOM) Y COSTOS")
        print("-" * 40)
        print(f" - Puntos de luz ({puntos_luz} un): ${subtotal_luz:.2f}")
        print(f" - Tomacorrientes ({tomas} un): ${subtotal_tomas:.2f}")
        print(f" - Tubería ({metros_tubo} m): ${subtotal_tuberia:.2f}")
        print(f" - Cableado estimado ({total_cable:.1f} m): ${subtotal_cable:.2f}")
        print("-" * 40)
        print(f"COSTO ESTIMADO TOTAL OBRA: ${total_general:.2f}")
    except ValueError:
        print("[Error] Datos de entrada incorrectos.")

def mallas_puesta_a_tierra():
    print("\n--- [3] DISEÑO Y VERIFICACIÓN DE MALLAS DE PUESTA A TIERRA (IEEE 80) ---")
    try:
        rho = float(input("Resistividad del suelo (Ohm-metro, ej. 100): "))
        A = float(input("Área aproximada de la malla (m²): "))
        L_total = float(input("Longitud total del conductor enterrado en la malla (m): "))
        
        if A <= 0 or L_total <= 0:
            print("[Error] El área y la longitud deben ser mayores a cero.")
            return
            
        # Fórmula empírica simplificada de resistencia de puesta a tierra (Sverak / IEEE 80)
        # R = rho * ( 1/L_total + 1/sqrt(20*A) * (1 + 1/(1 + h*sqrt(20/A))) ) -> Asumiendo h pequeño
        radio_equiv = math.sqrt(A / math.pi)
        R_malla = rho * ((1 / L_total) + (1 / (4 * radio_equiv)))
        
        print(f"\n[Resultado de Verificación]")
        print(f"Resistencia estimada de puesta a tierra: {R_malla:.2f} Ohmios")
        if R_malla <= 5.0:
            print("Diagnóstico: Cumple con la normativa típica de baja resistencia (< 5 Ohmios).")
        else:
            print("Diagnóstico: Resistencia elevada. Se requiere agregar jabalinas adicionales o tratamiento químico del suelo.")
    except ValueError:
        print("[Error] Ingrese valores numéricos válidos.")

def coordinacion_protecciones():
    print("\n--- [4] COORDINACIÓN DE PROTECCIONES DE SOBRECORRIENTE ---")
    print("Verificación de selectividad térmica/magnética básica entre interruptores.")
    try:
        I_cc_dispositivo = float(input("Corriente de cortocircuito en el punto de falla (A): "))
        In_aguas_abajo = float(input("Corriente nominal del interruptor secundario / carga (A): "))
        In_aguas_arriba = float(input("Corriente nominal del interruptor principal / protección aguas arriba (A): "))
        
        print(f"\n[Análisis de Selectividad]")
        if In_aguas_arriba > (1.5 * In_aguas_abajo):
            print("Selectividad por corriente: ACEPTABLE (Hay separación escalonada de calibres).")
        else:
            print("Advertencia: Margen muy estrecho entre protecciones; riesgo de disparo en cascada.")
            
        if I_cc_dispositivo < (In_aguas_arriba * 10):
            print("Curva magnética: El interruptor principal opera adecuadamente ante la falla evaluada.")
        else:
            print("Alerta: La corriente de falla supera la capacidad de respuesta inmediata estándar.")
    except ValueError:
        print("[Error] Ingrese datos numéricos correctos.")

def calculo_iluminacion():
    print("\n--- [5] CÁLCULO DE ILUMINACIÓN (MÉTODO DE LOS LÚMENES) ---")
    try:
        E = float(input("Iluminancia requerida (Luxes - ej. 300 para oficinas): "))
        largo = float(input("Largo del local (metros): "))
        ancho = float(input("Ancho del local (metros): "))
        lumenes_por_lampara = float(input("Flujo luminoso por lámpara/luminaria (Lúmenes): "))
        
        # Factores típicos de utilización y mantenimiento estimados
        cu_utilizacion = 0.60
        fp_mantenimiento = 0.80
        
        Area = largo * ancho
        # Fórmula: N = (E * Area) / (Phi * CU * FM)
        num_luminarias = (E * Area) / (lumenes_por_lampara * cu_utilizacion * fp_mantenimiento)
        
        print(f"\n[Resultado del Cálculo Lumínico]")
        print(f"Área del local: {Area:.2f} m²")
        print(f"Cantidad exacta teórica de luminarias requeridas: {num_luminarias:.2f}")
        print(f"Cantidad comercial sugerida a instalar: {math.ceil(num_luminarias)} unidades")
    except ValueError:
        print("[Error] Ingrese valores válidos.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == '1':
            simulador_cortocircuito()
        elif opcion == '2':
            generador_presupuestos_bom()
        elif opcion == '3':
            mallas_puesta_a_tierra()
        elif opcion == '4':
            coordinacion_protecciones()
        elif opcion == '5':
            calculo_iluminacion()
        elif opcion == '6':
            print("\nSaliendo del toolkit de protecciones. ¡Excelente trabajo por hoy, descansa bien!")
            sys.exit(0)
        else:
            print("[Error] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
