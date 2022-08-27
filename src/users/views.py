from django.shortcuts import render, get_object_or_404, redirect

from users.utils import password_verification_logic
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from common.models import Skill,Industry,Interest



class MyProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        template_name = "user/user-profile.html"
        current_user = User.objects.filter(username=username).first()
        current_profile = current_user.user_profile        
        return render(
            request,
            template_name,
            context={
                "current_user": current_user,
                "current_profile": current_profile,
                },
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
        current_user = User.objects.filter(username=request.user).first()
        current_profile = current_user.user_profile
        mentorship_sessions = request.user.mentorship_mentee.count()

        skills=Skill.objects.all()
        industries=Industry.objects.all()
        interests= Interest.objects.all()

        # industries

        return render(
            request,
            template_name,
            context={
                "current_user": current_user,
                "current_profile": current_profile,
                "skills": skills,
                "industries": industries,
                "mentorship_sessions":mentorship_sessions, 
                "interests": interests,
            },
        )

    def post(self, request, username):
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)

        if "personal-information" in request.POST:
            profile_pic = request.FILES.get("profile_pic", None)
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone = request.POST.get("phone")
            bio = request.POST.get("bio")
            # gender = request.POST.get("gender", None)
            user.first_name = first_name
            user.last_name = last_name
            profile.phone = phone
            profile.bio = bio
            if profile_pic is not None:
                profile.profile_pic = profile_pic
            profile.save()
            user.save()

        elif "change-password" in request.POST:
            cpass = request.POST.get("cpass")
            npass = request.POST.get("npass")
            vpass = request.POST.get("vpass")
            password = password_verification_logic(
                cpass,
                npass,
                vpass,
                request.user)
            success = password[0]
            message = password[1]
            
            if not success:
                messages.error(request, message)
                return redirect(
                    "users:edit-user-profile",
                    username=request.user.username)

        elif "professional-info" in request.POST:

            industries = request.POST.getlist("industries")
            interests = request.POST.getlist("interests")

            current_company = request.POST.get('current_company')
            current_job_role = request.POST.get('current_job_role')
            years_of_experience = request.POST.get('years_of_experience')

            profile.current_company = current_company 
            profile.current_job_role = current_job_role 
            profile.years_of_experience = years_of_experience

            for interest in interests:
                profile.interest.add(Interest.objects.get(id=interest))

            for industry in industries:
                profile.industry.add(Industry.objects.get(id=industry))
        
            profile.save()

            

            # industries =  request.POST.getlist('industries')
            # interests =  request.POST.getlist('interst')




                

            # profile.interst = interst 




        else:

            twitter = request.POST.get("twitter", "")
            github = request.POST.get("github", "")
            linkedin = request.POST.get("linkedin", "")
            personal = request.POST.get("personal", "")

            profile.twitter = twitter 
            profile.github = github
            profile.linkedin = linkedin 
            profile.personal_blog = personal
            profile.save()
        # profile.completed_profile = True
        # print(profile_pic)
        messages.success(request, "Profile updated successfully")
        return redirect("users:user-profile", username=request.user.username)
