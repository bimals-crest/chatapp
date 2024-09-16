from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('optin/', views.optin, name='optin'),
    path('optout/', views.optout, name='optout'),
    # Ensure this path is defined if you want to test the chat endpoint
    path('chat/', views.chat, name='chat'),
]
