import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RealTimeDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'data_updates'

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def data_update(self, event):
        message = event['message']

        # Send message to WebSocket client
        await self.send(text_data=json.dumps({
            'message': message
        }))
