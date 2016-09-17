from django.shortcuts import render_to_response
from django.template import RequestContext

def test_view(request):
    template = 'index.html'
    ctx = RequestContext(request, {})

    return render_to_response(template, ctx)
