from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^greeting/$', views.greeting, name = 'greeting'),
    url(r'^choice/$', views.choice, name = 'choice'),
    url(r'^normal_game/$', views.normal_game, name = 'normal_game'),
    url(r'^normal_game/(?P<id>[0-9]+)/$', views.normal_game, name = 'normal_game'),
    url(r'^hard_game/$', views.hard_game, name = 'hard_game'),
    url(r'^hard_game/(?P<id>[0-9]+)/$', views.hard_game, name = 'hard_game'),
    url(r'^hard_results/(?P<id>[0-9]+)/$', views.hard_results, name = 'hard_results'),
    url(r'^results/(?P<id>[0-9]+)/$', views.results, name = 'results'),
    url(r'^about/$', views.about, name = 'about'),
]