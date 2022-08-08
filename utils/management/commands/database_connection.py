import time

from django.db import connection, Error
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def log_console(self, message):
        self.stdout.write(message)
        self.stdout.flush()

    def handle(self, *args, **options):
        self.log_console("Waiting for database...")

        db_connected = None

        while not db_connected:
            try:
                connection.ensure_connection()
                db_connected = True
            except Error:
                self.log_console("Database unavailable, waiting 2 second...")
                time.sleep(2)

        self.log_console("Database available!")
