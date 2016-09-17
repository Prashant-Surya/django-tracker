import datetime
import json

from .queue import Queue

def track_click(request):
    import ipdb; ipdb.set_trace()
    data = request.POST
    kwargs = {
        'username': data['username'],
        'timestamp': str(datetime.datetime.now()),
        'url': data['url'],
        'track_type': 'Click',
        'data': {
            'identifier': data['identifier']
        }
    }
    queue = Queue('', 'visit')
    queue.push_message(json.loads(kwargs))

def track_link(request):
    data = request.POST
    kwargs = {
        'username': data['username'],
        'timestamp': str(datetime.datetime.now()),
        'url': data['url'],
        'track_type': 'Link',
        'data': {
            'identifier': data['identifier']
        }
    }
    queue = Queue('', 'visit')
    queue.push_message(json.loads(kwargs))