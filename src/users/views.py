from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class MyProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        template_name = "user/user-profile.html"
        current_user = User.objects.filter(username = username).first()
        current_profile = current_user.user_profile

        return render(
            request,
            template_name,
            context={"current_user": current_user, "current_profile": current_profile},
        )

    # def post(self, request):
    #     user = User.objects.get(username=request.user.username)
    #     profile = Profile.objects.get(user=user)
    #     profile_pic = request.FILES.get("profile_pic", None)
    #     university = request.POST.get("university")
    #     phone = request.POST.get("phone")
    #     bio = request.POST.get("bio")
    #     gender = request.POST.get("gender", None)
    #     twitter = request.POST.get("twitter")
    #     facebook = request.POST.get("facebook")
    #     profile.university = University.objects.get(id=university)
    #     profile.phone = phone
    #     profile.bio = bio
    #     profile.gender = gender
    #     profile.twitter = twitter
    #     profile.facebook = facebook
    #     profile.completed_profile = True
    #     print(profile_pic)
    #     if profile_pic is not None:
    #         profile.profile_pic = profile_pic
    #     profile.save()
    #     messages.success(request, "Profile updated successfully")
    #     return redirect("users:profile")





class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        template_name = "user/user-profile-edit.html"
        current_user = User.objects.filter(username = request.user).first()
        current_profile = current_user.user_profile

        return render(
            request,
            template_name,
            context={"current_user": current_user, "current_profile": current_profile},
        )

    def post(self, request, username):
        print(1)
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
        profile_pic = request.FILES.get("profile_pic", None)
        print(2)
        username = request.POST.get("username")

        print(3)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        gender = request.POST.get("gender", None)

        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        github = request.POST.get("github")
        linkedin    = request.POST.get("linkedin")                       
        personal_blog  = request.POST.get("personal_blog")

        check_username = User.objects.filter(username=username).first()

        print(7)

        if check_username:
            if check_username.id != request.user.id:
                
                messages.error(request, "Username unavailable please pick another username")
                return redirect("users:edit-user-profile", username=request.user.username)





        print(first_name, last_name, username)
        user.username = username

        user.first_name = first_name
        user.last_name = last_name
        profile.phone = phone
        profile.bio = bio
        profile.gender = gender

        # profile.github = github
        # profile.linkedin = linkedin
        # profile.personal_blog = personal_blog
        # profile.twitter = twitter
        # profile.facebook = facebook

        # profile.completed_profile = True
        # print(profile_pic)
        if profile_pic is not None:
            profile.profile_pic = profile_pic
        profile.save()
        user.save()
        messages.success(request, "Profile updated successfully")
        return redirect("users:user-profile", username= request.user.username)