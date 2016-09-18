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

    chart_data = [['URL', 'Visits']]

    for document in data:
        chart_data.append([
            str(document['_id']), int(document['count'])
        ])

    ctx = {
        'chart_data': chart_data
    }

    ctx = RequestContext(request, ctx)

    return render_to_response(template, ctx)


def fetch_clicks(request):
    template = 'clicks.html'
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
                    "_id": "$identifier",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]
    )

    chart_data = [['Identifier', 'Clicks']]

    for document in data:
        chart_data.append([
            str(document['_id']), int(document['count'])
        ])

    ctx = {
        'chart_data': chart_data
    }

    ctx = RequestContext(request, ctx)

    return render_to_response(template, ctx)