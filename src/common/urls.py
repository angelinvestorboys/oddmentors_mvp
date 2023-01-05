from django.urls import path
from .views import LoginView,RegisterView ,ResetPasswordView, ChangePasswordView, Logout,FAQView ,HowItWorksView, DashboardView, MySchedule, ExternalProfile,LandingView

app_name = "common"

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("myschedule/", MySchedule.as_view(), name="myschedule"),
    path("mentor/<str:username>", ExternalProfile.as_view(), name="external_profile"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("reset-password", ResetPasswordView.as_view(), name="reset-password"),
    path("change-password", ChangePasswordView.as_view(), name="change-password"),
    path("faq", FAQView.as_view(), name="faq"),
    path("how-it-works", HowItWorksView.as_view(), name="how-it-works"),
    path("logout", Logout, name="logout"),
]