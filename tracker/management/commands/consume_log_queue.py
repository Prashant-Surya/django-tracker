from django.core.management.base import BaseCommand

from tracker.queue import Queue

class Command(BaseCommand):
    """
    Worker to write logs into database
    """
    def handle(self, *args, **options):
        queue = Queue('', 'visit')
        queue.start_consuming()