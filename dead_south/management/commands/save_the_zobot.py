import sys
import json
from django.core.management.base import BaseCommand, CommandError
from dead_south.models import Article


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file')

    def handle(self, *args, **kwargs):
        filename = kwargs.get('file')
        with open(f'data/{filename}') as f:
            data = json.load(f)

        for article in data:
            Article.objects.get_or_create(
                source_text=article['source_text'],
                source_url=article['source_url'],
                output_text=list(filter(None, article['zobot'])),
                title=article['source_title']
            )
            