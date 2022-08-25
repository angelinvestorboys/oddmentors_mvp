
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .send_mail import send_mail

# Create your views here.
def dashboard(request):
    template_name = "dashboard.html"
    return render(request, template_name, context={})


def create_event(request):
    template_name = "create_event.html"
    return render(request, template_name, context={})



class LoginView(View):
    def get(self, request):
        template_name = "auth/login.html"
        if request.user.is_authenticated:
            return redirect("common:test")
        return render(request, template_name, context={})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Your account has been disabled.")
                return redirect("common:login")
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect("common:login")


class RegisterView(View):
    def get(self, request):
        template_name = "auth/register.html"
        if request.user.is_authenticated:
            return redirect("listings:home")
        return render(request, template_name, context={})

    def post(self, request):
        username = request.POST["registration_username"]
        email = request.POST["registration_email"]
        password = request.POST["registration_password"]
        first_name = request.POST["registration_first_name"]
        last_name = request.POST["registration_last_name"]
        try:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
            authenticate(username=username, password=password, email=email)
            send_mail(
                subject="STUGENT - Welcome Email",
                template_name="emails/welcome_email.html",
                context={"user": user},
                recipients=["adebisiayomide07@gmail.com", user.email],
            )
            messages.success(
                request,
                "Registration successful , please update your profile to continue and get the best service",
            )
            return redirect("users:profile")
        except Exception as e:
            print(e)
            messages.error(request, "a user with username or email already exists")
            return redirect("common:login")


class FAQView(View):
    def get(self, request):
        template_name = "common/faq.html"
        return render(request, template_name, context={})


class HowItWorksView(View):
    def get(self, request):
        template_name = "common/how_it_works.html"
        return render(request, template_name, context={})

class ResetPasswordView(View):
    def get(self, request):
        template_name = "common/reset-password.html"
        return render(request, template_name, context={})
    
    def post(self, request):
        # get email and send otp
        template_name = "common/reset-password.html"
        return render(request, template_name, context={})


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "common/change-password.html"
        return render(request, template_name, context={})

    def post(self, request):
        current_password = request.POST.get("current_password", None)
        new_password = request.POST.get("new_password", None)
        confirm_new_password = request.POST.get("confirm_new_password", None)
        if new_password != confirm_new_password:
            messages.error(request, "new password dosent match confirm new password")
            return redirect("common:change-password")
        user = authenticate(username=request.user.username, password=current_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            send_mail(
                subject="STUGENT - Change Password Successful",
                template_name="emails/change_password.html",
                context={"user": user},
                recipients=["adebisiayomide07@gmail.com", user.email],
            )
            messages.success(request, "Password Changed Successfully")
            return redirect("common:change-password")
        else:
            messages.error(request, "current password isnt correct")
            return redirect("common:change-password")


def Logout(request):
    logout(request)
    return redirect("common:login")