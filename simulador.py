import random
import asyncio
import websockets

async def enviar_nivel():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        nivel = 5.0
        while True:
            cambio=random.uniform(-0.3, 1.2)
            nivel += cambio
            nivel = max(0.0, min(nivel,30))
            await websocket.send(str(round(nivel,2)))
            print(f"Nivel enviado: {nivel:.2f} cm")
            await asyncio.sleep(2)  # Enviar cada 2 segundos
asyncio.run(enviar_nivel())
