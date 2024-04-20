from django.urls import path
from . import views

urlpatterns = [
    # path("chat/", views.chat, name="chat"),
    # path("ask_question/", views.ask_question, name="ask_question"),
    # path("chatbot_view/",views.chatbot_view,name="chatbot_view"),
    path('diet/', views.deit, name='deit'),
    # path('register/', views.register, name='register'),
    # path('ask_question/', views.ask_question, name='ask_question'),
]
