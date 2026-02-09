from django.core.management.base import BaseCommand
from django.core.management import call_command
from store.models import Product

class Command(BaseCommand):
    help = "Seed database with initial data if empty."

    def handle(self, *args, **options):
        if Product.objects.exists():
            self.stdout.write(self.style.SUCCESS("Seed skipped: products already exist."))
            return

        self.stdout.write("Seeding database from fixture...")
        call_command("loaddata", "store_data.json")
        self.stdout.write(self.style.SUCCESS("Seeding complete."))
