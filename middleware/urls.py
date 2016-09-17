from django.conf.urls import url

from .ajax_handlers import track_click, track_link

urlpatterns = [
    url(r'track-click/', track_click, name='track_click'),
    url(r'track-links/', track_link, name='track_link'),
]