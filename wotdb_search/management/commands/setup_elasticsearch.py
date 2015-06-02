from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import json, requests

class Command(BaseCommand):
    help = 'Sets up Elasticsearch for this app'

    def handle(self, *args, **options):
        # DROP INDEX IF POSSIBLE FIRST
        response = requests.delete(settings.ES_HOST + '/wotdb_character')

        # CREATE NEW INDEX
        data = {
            'dynamic': 'strict',
            'settings': {
                'number_of_shards': 1,
                'number_of_replicas': 1
            },
            'mappings': {
                'all': {
                    "properties": {
                        "name":              {'type': "string"},
                        "description":       {"type": "string"},
                        "gender":            {"type": "string"},
                        "title":             {"type": "string"},
                        "allegiance":        {"type": "string"},
                        "age":               {"type": "string"},
                        "alignment":         {"type": "string"},
                        "status":            {"type": "string"},
                        "clan":              {"type": "string"},
                        "clan_id":           {"type": "integer"},
                        "sept":              {"type": "string"},
                        "clan_id":           {"type": "integer"},
                        "channeler_type":    {"type": "string"},
                        "channeler_type_id": {"type": "integer"},
                        "society":           {"type": "string"},
                        "society_id":        {"type": "integer"},
                        "city":              {"type": "string"},
                        "city_id":           {"type": "integer"},
                        "country":           {"type": "string"},
                        "country_id":        {"type": "integer"},
                        "job":               {"type": "string"},
                        "job_id":            {"type": "integer"},

                    }
                }
            }
        }
        response = requests.put(settings.ES_HOST + '/wotdb_character/', data=json.dumps(data))
        print response.text
