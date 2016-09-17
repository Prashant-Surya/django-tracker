from pymongo import MongoClient

from django.shortcuts import render_to_response
from django.template import RequestContext


client = MongoClient()
db = client.tracker

# Create your views here

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
    count = 1
    for document in data:
        #print(document)
        graph_data.append({
            'x': count,
            'y': str(document['count'])
        })
        count += 1
    ctx = {
        'graph_data': graph_data
    }

    ctx = RequestContext(request, ctx)

    return render_to_response(template, ctx)