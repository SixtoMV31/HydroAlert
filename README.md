# HydroAlert 🌊

HydroAlert es un sistema de monitoreo y alerta temprana de inundaciones que permite medir el nivel del agua en tiempo real y mostrar alertas visuales según el riesgo detectado.

El proyecto está pensado para trabajar con un **ESP32 y sensores de nivel de agua**, pero actualmente incluye un **simulador** que reemplaza al microcontrolador para facilitar pruebas y desarrollo.

---

## 🎯 Objetivo del proyecto

Desarrollar un sistema capaz de:

* Medir el nivel del agua de forma continua
* Enviar los datos mediante **WebSockets**
* Visualizar el estado del nivel de agua en tiempo real
* Mostrar alertas cuando se detecten niveles peligrosos

---

## 🧠 Arquitectura del sistema

El sistema está compuesto por tres partes principales:

1. **ESP32 mostrando datos aleatoreos**

   * Simula el envío de datos del sensor de nivel de agua.
   * Envía los valores al servidor mediante WebSockets.

2. **Servidor WebSocket (Python)**

   * Recibe los datos del simulador (o ESP32 real).
   * Reenvía la información a los clientes conectados.

3. **Dashboard en Streamlit**

   * Recibe los datos en tiempo real.
   * Muestra el nivel del agua y el estado de alerta.

---

## 🗂️ Estructura del proyecto

```
HydroAlert/
├── app.py                 # Dashboard en Streamlit
├── websocket_server.py    # Servidor WebSocket
├── requirements.txt       # Dependencias del proyecto
├── .gitignore             # Archivos ignorados por Git
└── Sensor_Agua/
    └── Sensor_Agua.ino    # Código para el ESP32 (Arduino)
```

---

## ⚙️ Requisitos

* Python 3.10 o superior
* pip
* Entorno virtual (recomendado)

---

## 🚀 Instalación

Clona el repositorio:

```bash
git clone https://github.com/TU_USUARIO/HydroAlert.git
cd HydroAlert
```

Crea y activa el entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso del sistema

### 1 Dashboard Streamlit

```bash
streamlit run app.py
```
solo es necesario ejecutar esto ya que este archivo ejecuta el esp32_cliente dentro de el

Luego abre el navegador en:

```
http://localhost:8501
```

---

## 🚨 Niveles de alerta

* **Menor a 10 cm** → Nivel bajo control
* **Entre 10 y 20 cm** → Advertencia
* **Mayor a 20 cm** → ⚠️ Alerta de peligro

---

## 🔌 Integración con ESP32 (futuro)

Cuando se disponga del ESP32 y el sensor físico, el archivo `simulador.py` será reemplazado por el envío real de datos desde el microcontrolador, manteniendo intactos el servidor y el dashboard.

---

## 📌 Notas

* El entorno virtual (`venv`) no se incluye en el repositorio.
* Las dependencias se gestionan mediante `requirements.txt`.
* El proyecto está diseñado con fines académicos y de aprendizaje.

---

## 👤 Autor

Proyecto desarrollado como práctica de monitoreo de inundaciones usando Python, WebSockets y Streamlit.
