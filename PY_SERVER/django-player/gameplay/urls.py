from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import game_detail, make_move, AllGamesList


urlpatterns = [
    url(r'detail/(?P<id>\d+)/$',
        game_detail,
        name="gameplay_detail"),
    url(r'make_move/(?P<id>\d+)/',
        make_move,
        name="gameplay_make_move"),
    url(r'all$', AllGamesList.as_view())
]