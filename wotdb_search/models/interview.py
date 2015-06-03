from django.db import models
from elasticsearch import Elasticsearch

class Interview(models.Model):
    author   = models.CharField(max_length=100, default="Robert Jordan")
    question = models.TextField(default="")
    answer   = models.TextField(default="")
    name     = models.TextField(default="")
    date     = models.CharField(max_length=32, default="")

    def index_es(self):
        es = Elasticsearch()
        doc = self.build_payload()
        res = es.index(index="wotdb_interview",doc_type="all",id=self.id,body=doc)
        return res['created']

    def build_payload(self):
        doc = {
            'id': self.id,
            'name': self.name,
            'question': self.question,
            'answer': self.answer,
            'date': self.date,
        }
        return doc

    class Meta:
        app_label = "wotdb_search"
  