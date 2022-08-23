from django.db import models
from common.base_model import BaseModel
from django.contrib.auth.models import User

# Create your models here.


RATING = (
    (1, "1 Star"),
    (2, "2 Star"),
    (3, "3 Star"),
    (4, "4 Star"),
    (5, "5 Star"),
)

SESSION_TYPE = (
    ("One on One", "One On One"),
    ("Group", "Group")
)

class MentorshipSession(BaseModel):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentorship_mentee")
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentorship_mentor")
    session_duration = models.IntegerField(default=30, help_text="mentorship duration in minutes")
    meeting_location = models.TextField()
    session_review = models.TextField()
    session_rating = models.IntegerField(choices=RATING , null=True, blank=True)
    session_type = models.CharField(max_length=300 ,choices=SESSION_TYPE)


    def __str__(self):
        return f"Mentorship session between mentor {self.mentor.username} and mentee {self.mentee.username}"
    


class Scheduler(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentors_schedule")
    start_available_time = models.TimeField(null=True,blank=True)
    end_available_time = models.TimeField(null=True,blank=True)
