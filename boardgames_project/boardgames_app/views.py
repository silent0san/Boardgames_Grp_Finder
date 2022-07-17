from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MeetingForm

# Create your views here.


def home(request):
    return render(request, 'boardgames_app/home.html')


def add_meeting(request):
    submitted = False
    current_logged_user = request.user.username
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            saved_form_data = form.save(commit=False)
            saved_form_data.ownership = current_logged_user
            form.save()
            return redirect("/add_meeting?submitted=True")
    else:
        form = MeetingForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'boardgames_app/add_meeting.html', {"form": form, 'submitted': submitted})




