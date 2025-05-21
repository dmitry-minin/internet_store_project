import getpass

from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Command to create a superuser with a specified email and password.
    """
    help = "Create a superuser with a specified email and password."

    def handle(self, *args, **kwargs):
        while True:
            email = input("Enter email for superuser: ")
            email_confirm = input("Confirm email: ")
            if email != email_confirm:
                self.stdout.write(self.style.ERROR("Emails do not match. Please try again."))
                repeat = input("Do you want to try again? (y/n): ")
                if repeat.lower() != 'y':
                    break
                else:
                    continue
            break

        password = getpass.getpass("Enter password for superuser: ")
        password_confirm = getpass.getpass("Confirm password: ")
        if password != password_confirm:
            self.stdout.write(self.style.ERROR("Passwords do not match. Please try again."))
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR(f"User with email {email} already exists."))
            return

        user = User.objects.create(
            email=email,
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password(password)
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Superuser {email} created successfully."))
