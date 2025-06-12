from django.core.management.base import BaseCommand
from chat_app.models import Participant, Message

class Command(BaseCommand):
    help = 'Populates the database with initial data'
    
    def handle(self, *args, **options):
        # Clear existing data
        Participant.objects.all().delete()
        Message.objects.all().delete()
        
        # Create participants
        admin = Participant.objects.create(
            name='Admin'
        )

        azharr = Participant.objects.create(
            name='Azharr'
        )
        
        aceng = Participant.objects.create(
            name='Aceng'
        )
        
        ceng = Participant.objects.create(
            name='ceng'
        )
        
        alid = Participant.objects.create(
            name='Alid'
        )
        
        messages = []
        
        Message.objects.bulk_create(messages)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with initial data!')) 