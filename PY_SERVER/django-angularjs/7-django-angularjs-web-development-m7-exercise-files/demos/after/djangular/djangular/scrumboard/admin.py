from django.contrib import admin

from .models import List, Card, Project

admin.site.register(List)
admin.site.register(Card)
admin.site.register(Project)