from django.urls import path
from .views import EventDetail,SearchMentors

app_name = "events"

urlpatterns = [
    path("event/detail", EventDetail.as_view(), name="event_detail"),
    path("mentors/search", SearchMentors.as_view(), name="search_mentors"),
]