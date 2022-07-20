from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MeetingForm
from boardgames_project.boardgames_app.models import Meeting
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'boardgames_app/home.html')


@login_required(login_url='/login')
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


def meetings(request):
    all_meetings = Meeting.objects.all().order_by('meeting_name')

    return render(request, 'boardgames_app/meetings.html', {"all_meetings": all_meetings})


def show_meeting(request, meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)

    current_logged_user = request.user
    if current_logged_user in meeting.attendees.all():
        user_joined_meeting = True
        if request.GET.get('leave_status'):
            meeting.attendees.remove(current_logged_user)
            user_joined_meeting = False
            print(meeting.attendees.all())
    else:
        user_joined_meeting = False
        if request.GET.get('join_status'):
            meeting.attendees.add(current_logged_user)
            user_joined_meeting = True
            print(meeting.attendees.all())

    return render(request, 'boardgames_app/show_meeting.html', {'meeting': meeting,
                                                                'user_joined_meeting': user_joined_meeting})
