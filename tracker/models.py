from __future__ import unicode_literals

from mongoengine import Document, StringField, DictField, DateTimeField

#from django.db import models

# Create your models here.
class VisitLog(Document):
    username = StringField(max_length=200)
    url = StringField()
    data = DictField()
    timestamp = DateTimeField()
    identifier = StringField()
    track_type = StringField(max_length=10)

    meta = {'db_alias': 'tracker'}