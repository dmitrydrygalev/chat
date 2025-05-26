import socketio
from fastapi import FastAPI

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
sio_app = socketio.ASGIApp(sio, app)

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def chat_message(sid, data):
    print(f"Message from {sid}: {data}")
    await sio.emit('chat_message', data)



