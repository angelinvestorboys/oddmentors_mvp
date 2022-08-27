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

class SessionReview(BaseModel):
    review = models.TextField()
    rating = models.IntegerField(default=0)

class MentorshipSession(BaseModel):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentorship_mentor")
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentorship_mentee")
    duration = models.IntegerField(default=30, help_text="mentorship duration in minutes")
    location = models.TextField()
    details = models.TextField()
    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    review = models.ManyToManyField(SessionReview, related_name="session_reviews")
    session_rating = models.IntegerField(choices=RATING , null=True, blank=True)
    session_type = models.CharField(max_length=300 ,choices=SESSION_TYPE)
    completed_status = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Mentorship session between mentor {self.mentor.username} and mentee {self.mentee.username}"
    


class Scheduler(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mentors_schedule")
    start_available_time = models.TimeField(null=True,blank=True)
    end_available_time = models.TimeField(null=True,blank=True)
    update_reason = models.TextField()
