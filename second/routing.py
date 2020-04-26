from django.urls import path
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator , OriginValidator

from home.consumer import Chatconsumer

application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                    [
                    path('home/',Chatconsumer),
                ]
            )
        )
    )
})