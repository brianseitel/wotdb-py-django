from django.db import models
from elasticsearch import Elasticsearch

class Place(models.Model):

    class Meta:
        app_label = "wotdb_search"
  
    COUNTRY = "Country"
    CITY    = "City"
    PLACE_TYPES = (
        (COUNTRY, "Country"),
        (CITY, "City")
    )
    name        = models.CharField(max_length=100)
    place_type  = models.CharField(max_length=32,
                                  choices=PLACE_TYPES,
                                  null=True)
    ruler       = models.CharField(max_length=100, default="")
    allegiance  = models.CharField(max_length=100, default="None")
    description = models.TextField(default="")

    def __unicode__(self):
        return self.name

    def characters(self):
        from wotdb_search.models.character import Character
        return Character.objects.filter(country_id=self.id) | Character.objects.filter(city_id=self.id)

    def interviews(self, page):
        es = Elasticsearch()

        res = es.search(index="wotdb_interview",doc_type="all", body={
            "query": {
                "query_string": { "query": self.name }
            },
            "fields": ["id", "name", "question", "answer"],
            "size": 25,
            "from": 0
        })

        return res["hits"]["hits"]
