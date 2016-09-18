from django.conf.urls import url

from .ajax_handlers import track_click, track_link
from .views import fetch_visits, fetch_clicks

urlpatterns = [
    url(r'track-click/', track_click, name='track_click'),
    url(r'track-links/', track_link, name='track_link'),
    url(r'visits/', fetch_visits, name="fetch_visits"),
    url(r'clicks/', fetch_clicks, name="fetch_clicks"),
]