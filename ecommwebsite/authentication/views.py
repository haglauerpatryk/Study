from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]
        if password1 != password2:
            messages.warning(request, "Password does not match.")
            return render(request, "authentication/signup.html")
        try:
            if User.objects.get(username=email):
                messages.warning(request, "Email already exists.")
                return render(request, "authentication/signup.html")

        except Exception as identifier:
            pass

        user = User.objects.create_user(email, email, password1)
        user.save()
        return HttpResponse(f"User {email} created")
    return render(request, "authentication/signup.html")


def handle_login(request):
    if request.method == "POST":

        username = request.POST["email"]
        password1 = request.POST["pass"]
        myuser = authenticate(username=username, password=password1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Successfully logged in")
            return redirect(request, "/")

        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect(request, "/authentication/login")

    return render(request, "authentication/login.html")


def handle_logout(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect(request, "/login")
