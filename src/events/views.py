from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.

class EventDetail(View):
    def get(self, request):
        template_name = "event_detail.html"
        return render(request, template_name, context={})


class SearchMentors(View):
    def get(self, request):
        template_name = "search_mentors.html"
        return render(request, template_name, context={})