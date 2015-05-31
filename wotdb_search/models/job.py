from django.db import models
from elasticsearch import Elasticsearch

class Job(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(null=True)

    class Meta:
        app_label = "wotdb_search"
  
    def __unicode__(self):
        return self.name
