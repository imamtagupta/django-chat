# myproject/asgi.py
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path, re_path
# from myapp.consumers import ChatConsumer
# from myapp.myconsumer import ChatConsumer
from myapp.realtimeconsumer import RealTimeDataConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

print("Setting up the websocket url")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles traditional HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),  # Add your WebSocket route here
            re_path(r'ws/updates/', RealTimeDataConsumer.as_asgi()),  # Add your WebSocket route here
        ])
    ),
})
