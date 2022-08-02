

import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainSerializer


def index(request):
    """Главная страница"""
    return render(request, 'index.html', {})


def room(request, room_name):
    """"""
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

class CustomTokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name

        # ...

        return token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer