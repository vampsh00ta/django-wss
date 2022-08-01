from django.urls import path,re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import ChatConsumer

websockets = [

    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]