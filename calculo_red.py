def calcular_caida_tension():
    print("\n==================================================")
    print("   CALCULADOR DE CAIDA DE TENSION EN REDES")
    print("==================================================")
    
    try:
        # Datos de entrada
        sistema = input("¿El sistema es Monofásico (1) o Trifásico (3)?: ").strip()
        if sistema not in ['1', '3']:
            print("[X] Opción de sistema no válida.")
            return

        corriente = float(input("Corriente de carga (Amperios - A): "))
        longitud = float(input("Longitud del circuito (metros - m): "))
        seccion = float(input("Sección del conductor (mm²): "))
        tension_nominal = float(input("Voltaje nominal del sistema (Voltios - V): "))
        
        # Material del conductor
        print("Material del conductor:")
        print("1. Cobre (Cu)")
        print("2. Aluminio (Al)")
        op_mat = input("Selecciona material (1 o 2): ").strip()
        
        # Resistividad a 20°C (ohm * mm² / m)
        if op_mat == '1':
            rho = 0.0172  # Cobre
        elif op_mat == '2':
            rho = 0.0282  # Aluminio
        else:
            print("[X] Material no válido. Usando Cobre por defecto.")
            rho = 0.0172

        # Cálculo de resistencia total del conductor (ida y vuelta si es monofásico, o factor trifásico)
        if sistema == '1':
            # Monofásico: 2 * L * rho / S
            resistencia_total = (2 * longitud * rho) / seccion
            caida_v = corriente * resistencia_total
        else:
            # Trifásico aproximado: sqrt(3) * L * rho / S
            import math
            resistencia_total = (math.sqrt(3) * longitud * rho) / seccion
            caida_v = corriente * resistencia_total

        porcentaje_caida = (caida_v / tension_nominal) * 100

        # Resultados
        print("\n---------------- RESULTADOS ----------------")
        print(f"-> Resistencia del tramo: {resistencia_total:.4f} ohms")
        print(f"-> Caída de tensión absoluta: {caida_v:.2f} V")
        print(f"-> Caída de tensión porcentual: {porcentaje_caida:.2f}%")
        
        # Evaluación técnica estándar (generalmente se tolera hasta un 3% a 5% máximo)
        print("---------------- EVALUACIÓN ----------------")
        if porcentaje_caida <= 3.0:
            print("[✔] ESTADO: Óptimo. La caída está dentro del rango seguro (< 3%).")
        elif porcentaje_caida <= 5.0:
            print("[!] ESTADO: Aceptable para circuitos largos, pero al límite.")
        else:
            print("[X] ESTADO: Alerta. Caída excesiva (> 5%). Se recomienda subir la sección del conductor.")
        print("==================================================")

    except ValueError:
        print("[X] Error: Por favor ingresa solo valores numéricos válidos.")

if __name__ == "__main__":
    calcular_caida_tension()
