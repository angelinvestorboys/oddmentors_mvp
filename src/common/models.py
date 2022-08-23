from common.base_model import BaseModel
from django.db import models
from django.contrib.auth.models import User
from mentorship.models import MentorshipSession

class Notification(BaseModel):
    user = models.ForeignKey(User , related_name='user_notification', on_delete=models.CASCADE)
    action = models.TextField()


class PrivateMessage(BaseModel):
    mentor = models.ForeignKey(User , related_name='mentors_message', on_delete=models.CASCADE)
    mentee = models.ForeignKey(User , related_name='mentees_message', on_delete=models.CASCADE)
    mentorship_session = models.ForeignKey(MentorshipSession , related_name='mentorship_session', on_delete=models.CASCADE)
    action = models.TextField()


class Tag(BaseModel):
    name = models.TextField()

class Industry(BaseModel):
    name = models.TextField()


class Skill(BaseModel):
    name = models.TextField()

class Interest(BaseModel):
    name = models.TextField(help_text="intrests like swimming, fishing, etc")