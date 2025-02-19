from time import sleep
from django.db import connection
from django.core.management.base import BaseCommand, CommandParser
from zut.db import Db

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--max-retries', type=int, default=None)
        parser.add_argument('--migration', default=None, help="Example: `auth:0001_initial`")

    def handle(self, *, max_retries: int = None, migration: str = None, **options):
        current_retries = 0
        
        while not Db(connection).is_available(migration=migration):
            if not current_retries:
                msg = "Waiting for database"
                if migration:
                    msg += f" (migration \"{migration}\")"
                self.stdout.write(msg)
                self.stdout.flush()

                self.stdout.write("Retrying... ", ending='')
                self.stdout.flush()

            if max_retries is not None and current_retries >= max_retries:
                self.stdout.write(self.style.ERROR("NOT AVAILABLE"))
                exit(1)
            
            sleep(1)
            self.stdout.write(".", ending='')
            self.stdout.flush()
            current_retries += 1

        if current_retries:
            self.stdout.write(self.style.SUCCESS("OK"))
