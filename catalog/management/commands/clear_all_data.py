from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    """
    Command to clear all data from the database.
    """
    help = "Clear all data from the database."

    def handle(self, *args, **kwargs):
        """
        Handle the command.
        """
        try:
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("All data cleared successfully."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error clearing data: {e}"))
