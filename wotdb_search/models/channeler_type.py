from django.db import models
from elasticsearch import Elasticsearch

class ChannelerType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "wotdb_search"
  
    def __unicode__(self):
        return self.name
