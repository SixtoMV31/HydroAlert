import asyncio
import websockets
import json

nivel_actual = 0.0

async def escuchar_esp32():
    global nivel_actual
    uri = "ws://10.254.4.100:81"

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Conectado al ESP32")

                while True:
                    mensaje = await websocket.recv()
                    data = json.loads(mensaje)
                    nivel_actual = float(data["sensor"])
                    print("Nivel recibido:", nivel_actual)

        except Exception as e:
            print("Error de conexión:", e)
            await asyncio.sleep(5)
