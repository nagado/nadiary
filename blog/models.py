from __future__ import unicode_literals

from django.db import models

class Post(models.Model):

    id = models.IntegerField(primary_key=True)
    header = models.TextField()
    body = models.TextField()
    created = models.DateTimeField()
