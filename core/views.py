from django.shortcuts import render

# Create your views here.

def dashboard(request, *args, **kwargs):
    return render(request, "core/dashboard.html")

def request(request, *args, **kwargs):
    return render(request, "core/request.html")

def consultation(request, *args, **kwargs):
    return render(request, "core/consultation.html")
