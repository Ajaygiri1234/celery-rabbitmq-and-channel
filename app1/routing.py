from django.urls import re_path
from app1.consumer import TestConsumer

websocket_urlpatterns = [
    re_path(r"sock/",TestConsumer.as_asgi())
]


