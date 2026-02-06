import streamlit as st
import time
import websocket_server

st.set_page_config(page_title="Simulador de Inundación")
st.title("monigoreo del agua")
placeholder = st.empty()
while True:
    nivel = websocket_server.nivel_actual
    with placeholder.container():
        st.subheader(f"Nivel de agua actual (cm): {nivel:.2f}")
        if nivel < 10:
            st.success("Nivel de agua bajo control.")
        elif 10 <= nivel < 20:
            st.warning("Atención: Nivel de agua elevado.")
        else:
            st.error("¡Alerta! Nivel de agua crítico.")
    time.sleep(2)  # Actualizar cada 2 segundos