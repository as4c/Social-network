import json
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import User

class Command(BaseCommand):
    help = 'Load user data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file containing user data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, 'r') as file:
                users_data = json.load(file)
                
                for user_data in users_data:
                    user_data['password'] = make_password(user_data['password'])
                    User.objects.create(**user_data)
                
                self.stdout.write(self.style.SUCCESS('Successfully loaded user data'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
