from django.db import models


class Lunch(models.Model):
    nickname = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateField(auto_now=False,auto_now_add=False)


class Location(models.Model):
    lunch = models.ForeignKey(
        'Lunch',
        on_delete=models.CASCADE,
    )
    votes = models.IntegerField()
