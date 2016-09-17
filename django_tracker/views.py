from django.shortcuts import render_to_response
from django.template import RequestContext

from pymongo import MongoClient

client = MongoClient()
db = client.tracker

def test_view(request):
    template = 'index.html'
    ctx = RequestContext(request, {})

    return render_to_response(template, ctx)

def fetch_visits(request):
    template = 'visits.html'
    data = db.visit_log.aggregate(
        [
            {
                "$match":
                {
                     "track_type": "Visit"
                }
            },
            {
                "$group": {
                    "_id": "$url",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]
    )

    graph_data = []
    for document in data:
        #print(document)
        graph_data.append({
            'x': str(document['_id']),
            'y': int(document['count'])
        })

    ctx = {
        'graph_data': graph_data
    }

    ctx = RequestContext(request, ctx)

    return render_to_response(template, ctx)


def fetch_clicks(request):
    template = 'visits.html'
    data = db.visit_log.aggregate(
        [
            {
                "$match":
                {
                     "track_type": "Click"
                }
            },
            {
                "$group": {
                    "_id": "$url",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]
    )

    graph_data = []
    for document in data:
        #print(document)
        graph_data.append({
            'x': str(document['_id']),
            'y': int(document['count'])
        })

    ctx = {
        'graph_data': graph_data
    }

    ctx = RequestContext(request, ctx)

    return render_to_response(template, ctx)