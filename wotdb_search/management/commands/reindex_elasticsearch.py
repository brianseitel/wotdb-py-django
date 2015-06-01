from django.core.management.base import BaseCommand, CommandError
from wotdb_search.models import Character

class Command(BaseCommand):
    help = 'Sets up Elasticsearch for this app'

    def handle(self, *args, **options):
        characters = Character.objects.all()

        for character in characters:
            print "Indexing "+str(character.id)+ ": "+character.name
            character.index_es()

        print "Done\n"
