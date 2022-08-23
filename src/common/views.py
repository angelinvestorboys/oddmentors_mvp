from django.shortcuts import render

# Create your views here.
def test_view(request):
    template_name = "dashboard.html"
    return render(request, template_name, context={})

def login(request):
    template_name = "auth/login.html"
    return render(request, template_name, context={})