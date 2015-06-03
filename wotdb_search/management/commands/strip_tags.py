from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from wotdb_search.models import Character, Interview
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Sets up Elasticsearch for this app'

    def handle(self, *args, **options):
        characters = Character.objects.all()

        # for character in characters:
        #     character.description = self.strip_tags(character.description)
        #     character.save

        interviews = Interview.objects.all()
        for interview in interviews:
            question = self.strip_tags(interview.question)
            answer   = self.strip_tags(interview.answer)
            interview.question = question
            interview.answer   = answer
            interview.save()

    def strip_tags(self, doc):
        soup = BeautifulSoup(doc)
        text_parts = soup.get_text()
        doc = ''.join(text_parts)

        return doc