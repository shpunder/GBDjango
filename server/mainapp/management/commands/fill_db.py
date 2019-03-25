from django.core.management.base import BaseCommand
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        ShopUser.objects.create_superuser(
            'admin',
            'admin@admin.local',
            'admin',
            age=33)
