import streamlit as st

# --- FRONTSTAGE (Diseño de la página) ---
# Título principal con un emoji
st.title("🧙‍♂️ El Devorador de Vocales")

# Subtítulo explicativo
st.write("Escribe una palabra y el mago devorará sus vocales instantáneamente.")

# Caja de texto para que el usuario escriba la palabra
# El segundo parámetro "" es el valor por defecto (vacío)
user_word = st.text_input("Ingresa tu palabra aquí:", "")

# --- BACKSTAGE (Lógica en Python) ---
# El código solo se ejecutará si el usuario ha escrito algo
if user_word:
    # Convertimos la palabra a mayúsculas
    word_upper = user_word.upper()

    # Inicializamos contadores y listas
    cant_a = cant_e = cant_i = cant_o = cant_u = 0
    consonantes = []

    # El bucle que procesa la palabra
    for letter in word_upper:
        if letter == "A":
            cant_a += 1
        elif letter == "E":
            cant_e += 1
        elif letter == "I":
            cant_i += 1
        elif letter == "O":
            cant_o += 1
        elif letter == "U":
            cant_u += 1
        else:
            consonantes.append(letter)

    # --- MOSTRAR RESULTADOS EN LA PÁGINA ---
    st.subheader("--- RESULTADOS ---")

    # Uniendo las consonantes restantes
    letras_restantes = " ".join(consonantes)
    st.write(f"**Letras no consumidas (consonantes):** {letras_restantes}")

    # Armar la lista de vocales devoradas para mostrarla de forma limpia
    reporte_vocales = []
    if cant_a > 0:
        reporte_vocales.append(f"{cant_a} A")
    if cant_e > 0:
        reporte_vocales.append(f"{cant_e} E")
    if cant_i > 0:
        reporte_vocales.append(f"{cant_i} I")
    if cant_o > 0:
        reporte_vocales.append(f"{cant_o} O")
    if cant_u > 0:
        reporte_vocales.append(f"{cant_u} U")

    if reporte_vocales:
        # st.success muestra un recuadro verde muy bonito en la pantalla
        st.success(f"💥 ¡El mago devoró: {', '.join(reporte_vocales)}!")
    else:
        # st.info muestra un recuadro azul informativo
        st.info("🧙‍♂️ El mago se quedó con hambre... ¡No encontré ninguna vocal!")
