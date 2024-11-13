import random

# Lista de palabras posibles para el juego
palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]

# Selecciona una palabra al azar de la lista
palabra = random.choice(palabras).lower()
letras_adivinadas = set()  # Letras que el jugador ha adivinado
intentos_restantes = 6  # Intentos permitidos

print("¡Bienvenido al juego de ahorcado!")
print("_ " * len(palabra))

# Función para mostrar el progreso actual de la palabra
def mostrar_palabra():
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Bucle principal del juego
while intentos_restantes > 0:
    print("\nPalabra: ", mostrar_palabra())
    print(f"Intentos restantes: {intentos_restantes}")
    letra = input("Adivina una letra: ").lower()

    # Verifica si el jugador ingresó una letra válida
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue

    # Verifica si la letra ya fue adivinada
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue

    # Agrega la letra a las letras adivinadas
    letras_adivinadas.add(letra)

    # Verifica si la letra está en la palabra
    if letra in palabra:
        print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
    else:
        print(f"La letra '{letra}' no está en la palabra.")
        intentos_restantes -= 1

    # Verifica si el jugador ha ganado
    if all(letra in letras_adivinadas for letra in palabra):
        print("\n¡Felicidades! Has adivinado la palabra:", palabra)
        break
else:
    print("\nLo siento, te has quedado sin intentos. La palabra era:", palabra)
