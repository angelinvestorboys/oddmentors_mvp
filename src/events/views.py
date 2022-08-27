from .models import Event
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import EventCreationForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


class CreateEventView(View):
    template_name = "event/create_event.html"
    form = EventCreationForm()

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form })

    def post(self,request):
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = Event()
            event.user = request.user
            event.title = form.cleaned_data['title']
            event.event_date = form.cleaned_data['event_date']
            event.start_time = form.cleaned_data['start_time']
            event.end_time = form.cleaned_data['end_time']
            event.registration_link = form.cleaned_data['registration_link']
            event.meeting_link = form.cleaned_data['meeting_link']
            event.duration = form.cleaned_data['duration']
            event.location = form.cleaned_data['location']
            event.country = form.cleaned_data['country']
            event.state = form.cleaned_data['state']
            event.description = form.cleaned_data['description']
            event.save()
            messages.success(request, "Event has been successfully created")
            return redirect("common:dashboard")
        else:
            messages.success(request, "An error occoured")
            return render(request, self.template_name, context={'form': self.form})


def get_remaining_days_count(event_date):
    result = event_date.date() - datetime.now().date() 
    return result.days

class EventDetail(View):
    def get(self, request, pk):
        event = get_object_or_404(Event, id=pk)
        days_remaining = get_remaining_days_count(event.event_date)
        template_name = "event_detail.html"
        return render(request, template_name, context={"event":event, "days_remaining":days_remaining})


class SearchMentors(View):
    def get(self, request):
        template_name = "search_mentors.html"
        mentors = User.objects.all().exclude(id=request.user.id)
        return render(request, template_name, context={
            "mentors": mentors
        })