from django.core.management.base import BaseCommand
from userauths.models import CustomUser


class Command(BaseCommand):
    help = 'Reset all unusable passwords (marked with !) to allow users to log in'

    def add_arguments(self, parser):
        parser.add_argument(
            '--password',
            type=str,
            default='DefaultPass123!',
            help='Default password to set for users with unusable passwords'
        )

    def handle(self, *args, **options):
        password = options['password']
        users = CustomUser.objects.filter(password__startswith='!')
        count = users.count()

        if count == 0:
            self.stdout.write(self.style.SUCCESS('No users with unusable passwords found.'))
            return

        self.stdout.write(f'Found {count} users with unusable passwords.')
        self.stdout.write(f'Setting new password: {password}')

        for user in users:
            user.set_password(password)
            user.save()
            self.stdout.write(f'  ✓ Reset {user.username}')

        self.stdout.write(self.style.SUCCESS(f'Successfully reset {count} user password(s).'))
