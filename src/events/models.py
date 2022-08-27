from django.db import models
from django.contrib.auth.models import User
from common.base_model import BaseModel
from django_quill.fields import QuillField


LOCATION = (
    ("Online", "Online"),
    ("Onsite", "Onsite"),
)

class Event(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_creator"
    )
    title=models.CharField(max_length=200)
    description =QuillField()
    location = models.CharField(max_length=200, choices=LOCATION)
    meeting_link = models.CharField(max_length=200)
    registration_link = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=200, null=True)
    event_image = models.URLField()
    event_date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    completed_event = models.BooleanField(default=False)
    registered_users = models.ManyToManyField(User, related_name="event_attendees")

    def save(self, *args, **kwargs):
        # Add a custom logic here
        super(Event, self).save(*args, **kwargs)

    def get_registered_users_count(self, *args, **kwargs):
        registered_users_count = self.registered_users.count()
        return registered_users_count

    def __str__(self): 
        return self.title
