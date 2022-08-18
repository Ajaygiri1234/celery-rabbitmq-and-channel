import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import time


class TestConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, message):
        
        self.group_name="test"
        
        self.accept()
        
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        
        return await super().websocket_connect("message")
    

    async def receive_json(self, content, **kwargs):
        
        print("+"*50)
        print(content)
        print("+"*50)
        # time.sleep(10)
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type" :"functionname",
                "message":content,

            }
        
        )
    async def functionname(self, event):
        
        message = event["message"]
        await self.send(json.dumps(message))

        
    async def send_message(self, event):
        type = event.get('type')
        body = event.get('body')
        signal = event.get('signal')
        await self.send_json(
            {
                'body':"body",
                'signal':"signal",
            }
        )
        














'''
 1. setting: ASGI_APPLICATION = 'celerytest.asgi.application'
2.add channels to installed apps

3.replace application= get_asgi_application() with 
application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    })

##########################################
test server asgi/shannels will remove development server
4.write consumer in app


consumer.py
import json
from channels.generic.websocket import WebsockerConsumer,AsyncJsonWebsocketConsumer


class TestConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, message):
        self.accept()
        self.send(test_json=json.dumps({
            'type':"msg",
            'message':"hello"
        }
        ))

5. write routing.py 
from django.urls import re_path
from agent.consumer import TestConsumer

websocket_urlpatterns = [
    re_path(r"sock/",TestConsumer.as_asgi())
]


 '''       