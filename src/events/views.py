from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import EventCreationForm
# Create your views here.


class CreateEventView(View):
    def get(self, request):
        template_name = "event/create_event.html"
        return render(request, template_name, context={'form': EventCreationForm()})




class EventDetail(View):
    def get(self, request):
        template_name = "event_detail.html"
        return render(request, template_name, context={})


class SearchMentors(View):
    def get(self, request):
        template_name = "search_mentors.html"
        return render(request, template_name, context={})