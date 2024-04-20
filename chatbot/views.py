from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User

import google.generativeai as genai
from .models import Chat
from django.utils import timezone

google_api_key = 'AIzaSyCQTW839rZHeqC3rDv0rlKZRy2amBPtyls'
genai.configure(api_key=google_api_key)


def ask_gemini(message):
    
    model = genai.GenerativeModel('gemini-pro')  
    response = model.generate_content( message)
    return response.text.strip()

def chat(request):
    chats = Chat.objects.filter(user = request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemini(f"Generate a recipe for {message}")

        chat = Chat(user = request.user,message =message, response= response, created_at= timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat_app/chat.html', {'chats':chats})
