from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):
    """
    Custom command to load data from fixtures.
    """
    help = "Load data from fixtures."

    def add_arguments(self, parser):
        parser.add_argument(
            'fixtures',
            nargs='+',
            type=str,
            help="List of fixture files to load (e.g., 'categories.json products.json')."
        )

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        fixtures = options['fixtures']
        try:
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("All data cleared successfully."))

            for fixture in fixtures:
                call_command('loaddata', fixture)
                self.stdout.write(self.style.SUCCESS(f"Successfully loaded fixture: {fixture}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error clearing data: {e}"))
