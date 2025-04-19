from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command
from django.db import connection


class Command(BaseCommand):
    """
    Custom command to load data from fixtures.
    """
    help = " Delete all data from Product and Category models and reset sequences."


    def handle(self, *args, **options):
        """
        Handle the command.
        1 - Clear all data from Product and Category models.
        2 - Reset the sequences for Product and Category models.
        """
        try:
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("All data cleared successfully."))

            with connection.cursor() as cursor:
                cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
                cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            self.stdout.write(self.style.SUCCESS("Sequences reset successfully."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error clearing data: {e}"))
