from django.urls import path

from .views import test_view,login
app_name = "common"

urlpatterns = [
    path("", test_view, name="test"),
    path("login", login, name="login")
]