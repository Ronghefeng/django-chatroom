"""
ASGI config for django_chatroom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

# AuthMiddlewareStack将使用对当前经过身份验证的用户的引用来填充连接的scope, 类似于 Django 的request对象
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_chatroom.settings")

# channels的ProtocolTypeRouter会根据请求协议的类型来转发请求
application = ProtocolTypeRouter(
    {
        # http请求使用这个
        "http": get_asgi_application(),
        # websocket请求使用这个
        "websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
    }
)
