# django-chatroom

### gunicorn 托管项目支持 websocket
gunicorn django_chatroom.asgi:application -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000

### uWSGI 托管项目支持 websocket
启动：uwsgi --ini ./uwsgi.ini --http-websockets
停止：uwsgi --stop ./uwsgi.ini