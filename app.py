import streamlit as st
import time
import threading
import asyncio
import esp32_client

st.set_page_config(page_title="HydroAlert")
st.title("Monitoreo del Agua")

@st.cache_resource
def iniciar_websocket():
    hilo = threading.Thread(
        target=lambda: asyncio.run(esp32_client.escuchar_esp32()),
        daemon=True
    )
    hilo.start()
    return hilo

iniciar_websocket()

nivel = esp32_client.nivel_actual

st.subheader(f"Nivel de agua actual (cm): {nivel:.2f}")

if nivel < 10:
    st.success("Nivel de agua bajo control.")
elif nivel < 20:
    st.warning("Atención: Nivel de agua elevado.")
else:
    st.error("¡Alerta! Nivel de agua crítico.")

time.sleep(2)
st.rerun()
