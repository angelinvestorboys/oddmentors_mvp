from django.urls import path
from .views import LoginView,RegisterView ,ResetPasswordView, ChangePasswordView, Logout,FAQView ,HowItWorksView, home_view

app_name = "common"

urlpatterns = [
    path("", home_view, name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("reset-password", ResetPasswordView.as_view(), name="reset-password"),
    path("change-password", ChangePasswordView.as_view(), name="change-password"),
    path("faq", FAQView.as_view(), name="faq"),
    path("how-it-works", HowItWorksView.as_view(), name="how-it-works"),
    path("logout", Logout, name="logout"),
]