import random

def play_hangman(draw_text):
    """
    Función para jugar al ahorcado en un ambiente 3D.
    Utiliza la función draw_text para renderizar texto en el espacio 3D.

    Parámetros:
        draw_text (func): Función para dibujar texto en 3D. Debe aceptar los parámetros:
                          text, posX, posY, posZ, siceFont, R, G, B, RB, GB, BB.
    """
    # Palabras posibles
    word_list = ["robot", "tecnologia", "futuro", "python", "trixor", "openGL"]
    word_to_guess = random.choice(word_list).upper()
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    guessed_letters = set()

    # Posiciones para texto en el escenario
    text_positions = {
        "word": (-2, 2, -10),  # Palabra
        "message": (-2, 1, -10),  # Mensajes
        "attempts": (-2, 0, -10),  # Intentos restantes
        "letters": (-2, -1, -10),  # Letras usadas
    }

    # Función para renderizar el estado del juego
    def render_game():
        draw_text(" ".join(guessed_word), *text_positions["word"], 48, 255, 255, 255, 0, 0, 0)
        draw_text(f"Intentos restantes: {attempts}", *text_positions["attempts"], 36, 255, 255, 255, 0, 0, 0)
        draw_text(f"Letras usadas: {', '.join(sorted(guessed_letters))}", *text_positions["letters"], 24, 255, 255, 255, 0, 0, 0)
        if message:
            draw_text(message, *text_positions["message"], 36, 255, 0, 0, 0, 0, 0)

    # Mensaje inicial
    message = "Adivina la palabra"

    # Lógica principal del juego
    while attempts > 0 and "_" in guessed_word:
        render_game()
        # Esperar entrada del jugador
        player_input = input("Ingresa una letra: ").strip().upper()  # Esto debe ser manejado por tu sistema en 3D

        if len(player_input) != 1 or not player_input.isalpha():
            message = "Por favor, ingresa solo una letra válida."
            continue

        if player_input in guessed_letters:
            message = "Ya has intentado esa letra."
            continue

        guessed_letters.add(player_input)

        if player_input in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == player_input:
                    guessed_word[i] = player_input
            message = "¡Correcto!"
        else:
            attempts -= 1
            message = "Incorrecto."

    # Fin del juego
    if "_" not in guessed_word:
        message = f"¡Ganaste! La palabra era {word_to_guess}."
    else:
        message = f"Perdiste. La palabra era {word_to_guess}."
    render_game()
