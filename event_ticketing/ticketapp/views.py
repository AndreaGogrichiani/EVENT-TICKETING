from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import get_user_model
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'ticketapp/index.html')
    else:
        return redirect("home")

def error(request):
    return render(request, 'ticketapp/error.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'ticketapp/home.html')
    else:
        return redirect("index")

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, 'ticketapp/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                return redirect("error")
    else:
        form = LoginForm()

    return render(request, 'ticketapp/login.html', {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def events(request):
    events = Event.objects.all()

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("events")
    else:
        form = EventForm()

    return render(request, 'ticketapp/events.html', {'events': events, "form": form})


@login_required
def ticket(request, event_id):
    if request.method == "POST":
        event = Event.objects.get(id=event_id)
        user = get_user_model()
        Ticket.objects.create(event_title=event, user=user)
        return redirect('home')
    else:
        event = Event.objects.get(id=event_id)
        return render(request, 'ticketapp/events.html', {'event': event})
