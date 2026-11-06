import random
import string

def generar_password():
    print("--- GENERADOR DE CONTRASEÑAS SEGURAS ---")
    try:
        longitud = int(input("¿De cuántos caracteres la quieres? (ej. 12, 16): "))
        if longitud < 4:
            print("La longitud mínima recomendada es de 4 caracteres.")
            return

        usar_simbolos = input("¿Incluir símbolos especiales (!@#$%^&*)? (s/n): ").lower() == 's'

        # Construir el pool de caracteres
        caracteres = string.ascii_letters + string.digits
        if usar_simbolos:
            caracteres += "!@#$%^&*()-_+=<>?"

        # Asegurar al menos un elemento de cada tipo si se seleccionan símbolos
        password_list = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits)
        ]
        
        if usar_simbolos:
            password_list.append(random.choice("!@#$%^&*()-_+=<>?"))

        # Completar el resto de la longitud
        for _ in range(longitud - len(password_list)):
            password_list.append(random.choice(caracteres))

        # Mezclar para que no sea predecible
        random.shuffle(password_list)
        password_final = "".join(password_list)

        print(f"\nTu contraseña generada es:\n-> {password_final}\n")

    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    generar_password()
    