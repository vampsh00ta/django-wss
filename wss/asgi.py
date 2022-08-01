"""
ASGI config for wss project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""




import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from main.routing import websockets
from channels.auth import AuthMiddlewareStack
from .channelsmiddleware import TokenAuthMiddleware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wss.settings')


application = ProtocolTypeRouter({
    "websocket" : TokenAuthMiddleware(
        URLRouter(
           websockets,
        )
    ),
})







