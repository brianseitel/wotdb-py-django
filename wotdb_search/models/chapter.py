from django.db import models
from elasticsearch import Elasticsearch
from wotdb_search.models.book import Book

class Chapter(models.Model):
    number  = models.IntegerField(default=0)
    title   = models.CharField(max_length=100, default="")
    book    = models.ForeignKey(Book)

    class Meta:
        app_label = "wotdb_search"
  
    def characters(self):
        povs = PointOfView.objects.all().filter(chapter_id=self.id)
        return povs
