from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        email     = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 != password2:
            return HttpResponse('Incorrect Password')
            # return render(request, '/authentication/signup.html')
        try:
            if User.objects.get(username=email):
                return HttpResponse('Email already exists.')
                # return render(request, '/authentication/signup.html')
            
        except Exception as identifier:
            pass

        user = User.objects.create_user(email, email, password1)
        user.save()
        return HttpResponse('User created successfully')

def login(request):
    return render(request, 'authentication/login.html')

def logout(request):    
    return redirect(request, '/login')

