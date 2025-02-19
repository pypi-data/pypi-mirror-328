from time import sleep
from django.core.management.base import BaseCommand, CommandParser

from zut.django.tasks import demo

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--sync', action='store_true', help="Run task synchronously")
        parser.add_argument('--wait', action='store_true', help="Wait for the task to end (success, failure or revoked)")
        parser.add_argument('--countdown', type=int)
        parser.add_argument('--fail-at', type=int)

    def handle(self, *, sync = False, wait = False, fail_at: int = None, countdown: int = None, **options):
        if sync:
            demo(fail_at)
        else:
            result = demo.apply_async((fail_at,), countdown=countdown)
            print(f"Launched task {result.id} ({result.state})")
            if wait:
                while not result.ready():
                    sleep(1)
                    print(result.state, result.worker, result.date_done)
