import datetime

from middleware.queue import Queue

class RequestLogger(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_view(self, request, _view, *args, **kwargs):
        username = "Anonymous"
        if request.user.username:
            username = request.user.username
        kwargs = {
            'username': username,
            'timestamp': datetime.datetime.now(),
            'url': request.get_full_path(),
            'track_type': 'Visit',
            'data': {}
        }
        queue = Queue('', 'visit')
        queue.push_message('queue message')