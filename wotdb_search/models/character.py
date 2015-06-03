from django.db import models
from elasticsearch import Elasticsearch
from wotdb_search.models.channeler_type import ChannelerType
from wotdb_search.models.clan import Clan
from wotdb_search.models.job import Job
from wotdb_search.models.place import Place
from wotdb_search.models.sept import Sept
from wotdb_search.models.society import Society

class Character(models.Model):

    class Meta:
        app_label = "wotdb_search"
  
    # Genders
    MALE   = "Male"
    FEMALE = "Female"
    OTHER  = "Other"

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )

    # Alignments
    LIGHT  = "Light"
    DARK   = "Dark"
    NEUTRAL = "Neutral"

    ALIGNMENTS = (
        (LIGHT, "Light"),
        (DARK,  "Dark"),
        (NEUTRAL, "Neutral")
    )

    # Statuses
    ALIVE   = "Alive"
    DEAD    = "Dead"
    UNKNOWN = "Unknown"

    STATUSES = (
        (ALIVE, "Alive"),
        (DEAD, "Dead"),
        (UNKNOWN, "Unknown")
    )

    # Fields
    name        = models.CharField(max_length=100)
    description = models.TextField(default="")
    gender      = models.CharField(max_length=16, default="")
    title       = models.CharField(max_length=64, default="")
    allegiance  = models.CharField(max_length=32, default="")
    age         = models.IntegerField(default=0)
    alignment   = models.CharField(max_length=32,
                                   choices=ALIGNMENTS,
                                   default=NEUTRAL)
    status      = models.CharField(max_length=32,
                                   choices=STATUSES,
                                   default=UNKNOWN)

    # Relationships
    channeler_type = models.ForeignKey(ChannelerType, null=True)
    clan           = models.ForeignKey(Clan,          null=True)
    job            = models.ForeignKey(Job,           null=True)
    sept           = models.ForeignKey(Sept,          null=True)
    society        = models.ForeignKey(Society,       null=True)
    city           = models.ForeignKey(Place,         null=True, related_name="city")
    country        = models.ForeignKey(Place,         null=True, related_name="country")

    def __unicode__(self):
        return self.name;

    def is_alive(self):
        return self.status == self.ALIVE

    def is_aiel(self):
        return self.sept or self.clan or self.society

    def index_es(self):
        es = Elasticsearch()
        doc = self.build_payload()
        res = es.index(index="wotdb_character",doc_type="all",id=self.id,body=doc)
        return res['created']

    def build_payload(self):
        doc = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'gender': self.gender,
            'title': self.title,
            'allegiance': self.allegiance,
            'age': self.age,
            'alignment': self.alignment,
            'status': self.status,
        }

        if (self.clan):
            doc['clan'] = self.clan.name
            doc['clan_id'] = self.clan_id

        if (self.sept):
            doc['sept'] = self.sept.name
            doc['sept_id'] = self.sept_id

        if (self.channeler_type):
            doc['channeler_type'] = self.channeler_type.name
            doc['channeler_type_id'] = self.channeler_type_id

        if (self.society):
            doc['society'] = self.society.name
            doc['society_id'] = self.society_id

        if (self.city):
            doc['city'] = self.city.name
            doc['city_id'] = self.city_id

        if (self.country):
            doc['country'] = self.country.name
            doc['country_id'] = self.country_id

        if (self.job):
            doc['job'] = self.job.name
            doc['job_id'] = self.job_id

        return doc

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
