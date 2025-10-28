from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')
def signup(request):
    return render(request, 'signup.html')
def map(request):
    return render(request, 'map.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def swap(request):
    return render(request, 'swap.html')
def profile(request, user_id):
    return render(request, 'profile.html')
def feed(request):
    return render(request, 'feed.html')
def projects(request):
    return render(request, 'projects.html')
def events(request):
    return render(request, 'events.html')
def explore(request):
    return render(request, 'explore.html')
def resources(request):
    return render(request, 'resources.html')
def mybookings(request):
    return render(request, 'mybookings.html')
def credits(request):
    return render(request, 'credot.html')
def meet(request):
    return render(request, 'meet.html')
def profile3(request):
    return render(request, 'profile3.html')