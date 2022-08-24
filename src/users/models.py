from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import string, random
from common.base_model import BaseModel
from events.models import Event
from common.models import Skill,Industry,Interest
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

# function to generate a random value
def refferal_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class Profile(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    nickname = models.TextField()
    bio = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    profile_pic = models.URLField(default = "")
    phone = models.CharField(max_length=20, null=True)
    industry = models.ManyToManyField(Industry, related_name="user_industries")
    years_of_experience = models.IntegerField(default=0)
    interest = models.ManyToManyField(Interest, related_name="user_interests")
    skills = models.ManyToManyField(Skill, related_name="user_skills")
    completed_profile = models.BooleanField(default=False)
    current_job_role = models.CharField(max_length=10, null=True)
    current_company = models.CharField(max_length=10, null=True)
    user_rating = models.CharField(max_length=10, null=True)
    refferal_code = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=200, default="https://www.twitter.com/")
    github = models.CharField(max_length=200, default="https://www.twitter.com/")
    facebook = models.CharField(max_length=200, default="https://www.facebook.com/")
    linkedin = models.CharField(max_length=200, default="https://www.linkedin.com/")
    personal_blog = models.CharField(max_length=200, default="https://www.facebook.com/")

    def save(self, *args, **kwargs):
        # Add a logic to check if refferal code already exists
        if self.refferal_code == None:
            self.refferal_code = refferal_code_generator()
        # add logic to update completed_profile field if the fields are completed
        super(Profile, self).save(*args, **kwargs)

    def get_user_events(self, *args, **kwargs):
        all_listings = Event.objects.filter(realtor=self.user)
        return all_listings

    def get_user_upcoming_events(self, *args, **kwargs):
        upcoming_listings = Event.objects.filter(realtor=self.user)
        return upcoming_listings

    def get_user_listings(self, *args, **kwargs):
        all_listings_count = Event.objects.filter(realtor=self.user).count()
        return all_listings_count

    def __str__(self):  # Show name as the identifying field
        return "{}'s Profile".format(self.user.username)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=kwargs.get("instance"))