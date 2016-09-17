from __future__ import unicode_literals

from mongoengine import Document, StringField, DictField

#from django.db import models

# Create your models here.
class RequestLog(Document):
    user_name = StringField(max_length=200)
    url = StringField()
    data = DictField()