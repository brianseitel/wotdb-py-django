from django.db import models
from elasticsearch import Elasticsearch
from wotdb_search.models.clan import Clan

class Sept(models.Model):
    name = models.CharField(max_length=100)
    clan = models.OneToOneField(Clan)

    class Meta:
        app_label = "wotdb_search"
  
    def __unicode__(self):
        return self.name
