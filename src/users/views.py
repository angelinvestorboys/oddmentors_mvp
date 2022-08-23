from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from common.models import Bookmark
from django.views.generic import View
from django.contrib import messages
from common.models import University
from django.contrib.auth.mixins import LoginRequiredMixin


class MyProfileView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "users/my-profile.html"
        profile = get_object_or_404(Profile, user=request.user)
        universities = University.objects.all()
        return render(
            request,
            template_name,
            context={"profile": profile, "universities": universities},
        )

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
        profile_pic = request.FILES.get("profile_pic", None)
        university = request.POST.get("university")
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        gender = request.POST.get("gender", None)
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        profile.university = University.objects.get(id=university)
        profile.phone = phone
        profile.bio = bio
        profile.gender = gender
        profile.twitter = twitter
        profile.facebook = facebook
        profile.completed_profile = True
        print(profile_pic)
        if profile_pic is not None:
            profile.profile_pic = profile_pic
        profile.save()
        messages.success(request, "Profile updated successfully")
        return redirect("users:profile")