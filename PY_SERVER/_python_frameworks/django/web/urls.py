from django.conf.urls import url

from web.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
