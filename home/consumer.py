import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from .models import Following_list,Post


class Chatconsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("connected",event)
        user = self.scope['user']
        print(user)
        following_list = await self.get_following_list(user)
        for following in following_list :
            room = f"room.{following}"
            await self.channel_layer.group_add(
                room,
                self.channel_name
            )
            print(f"Added {self.channel_name} to group {room}")
        await self.send({
            "type" : "websocket.accept",
        }
        )
 
    async def websocket_receive(self,event):
        print("recieved",event)

        msg = event.get('text', None)
        if msg is not None :
            loaded_dict_data = json.loads(msg)
            user = self.scope['user']
            msg_data = loaded_dict_data.get('message')
            response = {

                'message' : msg_data,
                'username' : user.username

            }

            await self.save_post(user,msg_data)

            await self.channel_layer.group_send(
                f"room.{user.username}",
                {
                    "type":"posting",
                    "message":"post"
                }
            )
    async def posting(self,event) :
        print("hey",event)

    async def websocket_disconnect(self,event):
        print("disconnected",event)

    @database_sync_to_async
    def get_following_list(self,user) :
        querry_list = Following_list.following_list(Following_list,user)
        actual_list = []
        for followings in querry_list :
            actual_list.append(followings.following.username)
        return actual_list
    
    @database_sync_to_async
    def save_post(self,user,post_txt):
        post = Post.objects.create(postid=user,text=post_txt)

        
