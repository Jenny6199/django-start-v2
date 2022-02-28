from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'create superuser'

    def handle(self,*args, **options):
        User.objects.create_superuser(
            username='django',
            email='django@geekbrains.local',
            password='geekbrains',
        )
