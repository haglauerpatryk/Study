from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, \
                              urlsafe_base64_decode
from .utils import generate_token, TokenGenerator
from django.utils.encoding import force_bytes, force_str, \
                                  DjangoUnicodeDecodeError
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

# Create your views here.


def signup(request):
    if request.method == "POST":
        email     = request.POST["email"]
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
        user.is_active = False
        user.save()
        email_subject = "Activate your account"
        message = render_to_string("authentication/activate.html",{
                "user"  : user,
                "domain": request.META["HTTP_HOST"],
                "uid"   : urlsafe_base64_encode(force_bytes(user.pk)),
                "token" : generate_token.make_token(user),
        })

        connection = get_connection(username=settings.EMAIL_HOST_USER,
                                    password=settings.EMAIL_HOST_PASSWORD, 
                                    ssl=None)
        email_message = EmailMessage(email_subject, message, 
                                     settings.EMAIL_HOST_USER, [email], 
                                     connection=connection)
        email_message.send()
        messages.success(request, "Account created successfully. Please \
                                   check your email to activate your account.")
        return redirect("/authentication/login")
    return render(request, "authentication/signup.html")

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully.")
            return redirect("/authentication/login")
        return render(request, "authentication/activate_failed.html")

def handle_login(request):
    if request.method == "POST":

        username = request.POST["email"]
        password1 = request.POST["pass1"]
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
    return redirect(request, "authentication/login")
