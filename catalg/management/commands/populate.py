from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run all populate commands together'

    def handle(self, *args, **kwargs):
        # List of commands to be executed
        commands = [
            'populate_categories',
            'populate_colors',
            'populate_District',
            'populate_item_types',
            'populate_ratings',
            'generate_items',
            'populate_sizes',
        ]

        # Loop through and call each command
        for command in commands:
            try:
                self.stdout.write(f'Running {command}...')
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f'Successfully executed {command}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error while executing {command}: {str(e)}'))

