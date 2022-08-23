from django.db import models
from django.contrib.auth.models import User
from common.base_model import BaseModel

LOCATION = (
    ("Online", "Online"),
    ("Onsite", "Onsite"),
)

class Event(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="event_creator"
    )
    title = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=200, choices=LOCATION)
    meeting_link = models.TextField()
    profile_pic = models.TextField()
    phone = models.CharField(max_length=20)
    completed_profile = models.BooleanField(default=False)
    refferal_code = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=200, default="https://www.twitter.com/")
    registered_users = models.ManyToManyField(User, related_name="event_attendees")

    def save(self, *args, **kwargs):
        # Add a custom logic here
        super(Event, self).save(*args, **kwargs)

    def get_registered_users_count(self, *args, **kwargs):
        registered_users_count = self.registered_users.count()
        return registered_users_count

    def __str__(self): 
        return self.title
