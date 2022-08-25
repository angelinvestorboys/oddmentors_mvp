
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .send_mail import send_mail
from string import ( punctuation, whitespace, digits, ascii_lowercase, ascii_uppercase)



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
            return redirect("common:home")
        return render(request, template_name, context={})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/dashboard")
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
            return redirect("common:home")
        return render(request, template_name, context={})

    def post(self, request):
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"].strip()
        password2 = request.POST["password2"].strip()
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]

        if password != password2:
            messages.error(request, "passwords inputed do not match")
            return redirect("common:register")

        if not self.is_valid_password(password):
            messages.error(request, "password must contain  a minimum of 6 characters (a combination of Uppercase and lower case characters and a digit)")
            return redirect("common:register")

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
            # send_mail(
            #     subject="STUGENT - Welcome Email",
            #     template_name="emails/welcome_email.html",
            #     context={"user": user},
            #     recipients=["adebisiayomide07@gmail.com", user.email],
            # )
            messages.success(
                request,
                "Registration successful , please update your profile to continue and get the best service",
            )
            return redirect("common:home")
        except Exception as e:
            messages.error(request, "a user with username or email already exists")
            return redirect("common:register")




    def is_valid_password(self, password):
        new_password = password.strip()

        MIN_SIZE = 6
        MAX_SIZE = 20
        password_size = len(new_password)

        if password_size < MIN_SIZE or password_size > MAX_SIZE:
            return False

        # valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
        # invalid_chars = set(punctuation + whitespace) - valid_chars

        # for char in invalid_chars:
        #     if char in new_password:
        #         return False

        password_has_digit = False

        for char in password:
            if char in digits:
                password_has_digit = True
                break

        if not password_has_digit:
            return False

        password_has_lowercase = False

        for char in password:
            if char in ascii_lowercase:
                password_has_lowercase = True
                break

        if not password_has_lowercase:
            return False


        password_has_uppercase = False

        for char in password:
            if char in ascii_uppercase:
                password_has_uppercase = True
                break

        if not password_has_uppercase:
            return False

        return True


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
        template_name = "auth/reset_password.html"
        return render(request, template_name, context={})
    
    def post(self, request):
        # get email and send otp

        template_name = "auth/reset_password.html"

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