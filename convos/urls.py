from django.urls import path, include
from . import views


urlpatterns = [
    path('chat/', views.index,name='chats'),
    path('my-convos/<int:user_id>', views.get_convos),
    # path('chat/', views.create_message_fb,name="chats"),
    
    path('get-messages/<slug:convo_uuid>', views.get_messages),
    path('send-message/<slug:convo_uuid>', views.create_message),
    # path('send-message-fb', views.create_message_fb),
]