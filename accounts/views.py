from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'accounts/login.html')

def register_page(request):
    
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
    
    
    
    
    return render(request,'accounts/register.html')