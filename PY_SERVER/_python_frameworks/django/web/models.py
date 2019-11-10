from django.db import models


class Note(models.Model):

    note = models.CharField(max_length=250)
