import datetime
import json

from django.http import HttpResponse

from .queue import Queue

def track_click(request):
    data = request.POST
    kwargs = {
        'username': data.get('username'),
        'timestamp': str(datetime.datetime.now()),
        'url': data.get('location'),
        'track_type': 'Click',
        'data': {
            'identifier': data.get("identifier")
        }
    }
    queue = Queue('', 'visit')
    queue.push_message(json.dumps(kwargs))
    return HttpResponse("Hola! Surya")

def track_link(request):
    data = request.POST
    kwargs = {
        'username': data.get('username'),
        'timestamp': str(datetime.datetime.now()),
        'url': data.get('location'),
        'track_type': 'Link',
        'data': {
            'identifier': data.get('identifier')
        }
    }
    queue = Queue('', 'visit')
    queue.push_message(json.dumps(kwargs))
    return HttpResponse("Hola")