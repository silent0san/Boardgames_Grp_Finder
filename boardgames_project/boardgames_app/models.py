from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    meeting_name = models.CharField('Meeting Name', max_length=150, default='')
    game_name = models.CharField('Game Name', max_length=150, default='')
    meeting_date = models.DateField(default='')
    meeting_hour = models.TimeField(auto_now=False, auto_now_add=False, default='', blank=True)
    current_amount_of_players = models.PositiveSmallIntegerField(blank=True)
    wanted_amount_of_players = models.PositiveSmallIntegerField()
    city = models.CharField('City', max_length=100, default='')
    address = models.CharField('Address', max_length=150, default='', blank=True)
    zip_code = models.CharField('Zip Code', max_length=10, default='')
    attendees = models.ManyToManyField(User, blank=True)
    ownership = models.CharField(max_length=150, default='', blank=False)

    def __str__(self):
        return self.meeting_name

