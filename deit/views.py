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

def diet(request):
    chats = Chat.objects.filter(user = request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        if message.startswith('Find refernce link for these dish:'):
            response = ask_gemini(f"Find reference link for these dish :{message}")
        elif message.startswith('Added ingredients:'):
            response = ask_gemini(f"recommend one word list of names of dish based on these available ingridents :{message}")
        elif message.startswith('Added dietary restrictions:'):
            response = ask_gemini(f"recommend one word list of names of dish that can we prepared having these dietary restrictions :{message}")
        else:
            response = ask_gemini(f"Write a paragraph for the recipe of these dish:{message}")

        chat = Chat(user = request.user,message =message, response= response, created_at= timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'deit/index.html', {'chats':chats})
