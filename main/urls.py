from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from . import views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('api/v1/token/',CustomTokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/token/verify/', TokenVerifyView.as_view()),

]