from django.contrib import admin

from mentorship.models import SessionReview,Scheduler,MentorshipSession

# Register your models here.
admin.site.register(SessionReview)
admin.site.register(Scheduler)
admin.site.register(MentorshipSession)