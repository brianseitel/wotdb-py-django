from django.db import models
from elasticsearch import Elasticsearch

class Interview(models.Model):
    author   = models.CharField(max_length=100, default="Robert Jordan")
    question = models.TextField(default="")
    answer   = models.TextField(default="")
    name     = models.TextField(default="")
    date     = models.CharField(max_length=32, default="")

    class Meta:
        app_label = "wotdb_search"
  