from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return "Project: {}".format(self.name)


@python_2_unicode_compatible
class List(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, related_name='lists')

    def __str__(self):
        return "List: {}".format(self.name)


@python_2_unicode_compatible
class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name="cards")
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return "Card: {}".format(self.title)

