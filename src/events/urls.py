from django.urls import path
from .views import EventDetail,SearchMentors, CreateEventView

app_name = "events"

urlpatterns = [
    path("detail", EventDetail.as_view(), name="event_detail"),
    path("mentors/search", SearchMentors.as_view(), name="search_mentors"),
    path("create", CreateEventView.as_view(), name="create_event"),
]