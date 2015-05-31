from django.db import models
from elasticsearch import Elasticsearch
from wotdb_search.models.character import Character
from wotdb_search.models.book import Book
from wotdb_search.models.chapter import Chapter

class PointOfView(models.Model):
    character = models.ForeignKey(Character)
    book      = models.ForeignKey(Book)
    chapter   = models.ForeignKey(Chapter)

    class Meta:
        app_label = "wotdb_search"
  