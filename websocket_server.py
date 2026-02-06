import asyncio
import websockets

nivel_actual = 0.0

async def handler(websocket):
    global nivel_actual
    async for message in websocket:
        nivel_actual = float(message)
        print(f"Nivel actual recibido: {nivel_actual}")
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("servidor WebSocket iniciado en puerto 8765")
        await asyncio.Future() 
if __name__ == "__main__":
    asyncio.run(main())