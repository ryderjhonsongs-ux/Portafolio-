def calcular_ohm():
    print("--- CALCULADORA ELÉCTRICA (Ley de Ohm) ---")
    print("Ingresa '?' en el valor que quieras calcular.")
    
    try:
        v = input("Voltaje (V en Volts): ")
        i = input("Corriente (I en Amperes): ")
        r = input("Resistencia (R en Ohms): ")

        if v == '?':
            i, r = float(i), float(r)
            resultado = i * r
            print(f"\n[Resultado] Voltaje (V) = {resultado:.2f} V")
        elif i == '?':
            v, r = float(v), float(r)
            if r == 0:
                print("Error: La resistencia no puede ser cero.")
                return
            resultado = v / r
            print(f"\n[Resultado] Corriente (I) = {resultado:.4f} A")
        elif r == '?':
            v, i = float(v), float(i)
            if i == 0:
                print("Error: La corriente no puede ser cero.")
                return
            resultado = v / i
            print(f"\n[Resultado] Resistencia (R) = {resultado:.2f} Ohms")
            
            # Extra: Calcular potencia si ya tenemos V e I o R
            potencia = v * i
            print(f"[Extra] Potencia disipada (P) = {potencia:.2f} W")
        else:
            print("No seleccionaste ninguna incógnita ('?').")
            
    ValueError:
        print("Por favor, ingresa números válidos.")

if __name__ == "__main__":
    calcular_ohm()
    