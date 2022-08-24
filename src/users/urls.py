from django.urls import path
from .views import MyProfileView, EditProfileView

app_name = "users"

urlpatterns = [
    path("<str:username>", MyProfileView.as_view(), name="user-profile"),

    path("edit/<str:username>", EditProfileView.as_view(), name="edit-user-profile"),



    
]

