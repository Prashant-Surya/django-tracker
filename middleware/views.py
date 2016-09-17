from pymongo import MongoClient
client = MongoClient()
db = client.tracker

# Create your views here.


def fetch_data(request):
    data = db.tracker.aggregate(
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
    for document in data:
        print(document)
