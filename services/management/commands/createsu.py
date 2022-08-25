import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

password = os.environ['NWM_SUPASSWORD']

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@admin.com", password)