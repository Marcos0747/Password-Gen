import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    print("Genera contraseñas seguras")

    while True:
        longitud = int(input("Ingresa la longitud de la contraseña deseada: "))

        if longitud <= 0:
            print("La longitud debe ser mayor que cero. Inténtalo nuevamente.")
        else:
            contrasena_generada = generar_contrasena(longitud)
            print(f"Contraseña generada: {contrasena_generada}")
            break
