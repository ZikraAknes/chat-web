from django.core.management.base import BaseCommand
from chat_app.models import Participant, Message

class Command(BaseCommand):
    help = 'Populates the database with initial data'
    
    def handle(self, *args, **options):
        # Clear existing data
        Participant.objects.all().delete()
        Message.objects.all().delete()
        
        # Create participants
        john = Participant.objects.create(
            name='John'
        )
        
        sarah = Participant.objects.create(
            name='Sarah'
        )
        
        mike = Participant.objects.create(
            name='Mike'
        )
        
        emma = Participant.objects.create(
            name='Emma'
        )
        
        # Create messages
        messages = [
            Message(
                participant=john,
                content='Hey everyone! How are you all doing?',
                message_type='text',
                delay=1000
            ),
            Message(
                participant=sarah,
                content='Hi John! I\'m good, just got back from my trip.',
                message_type='text',
                delay=3000
            ),
            Message(
                participant=mike,
                content='Hello everyone! Check out this video from my vacation:',
                message_type='text',
                delay=5000
            ),
            Message(
                participant=mike,
                content='/static/chat_app/videos/sample1.mp4',
                message_type='video',
                delay=6000
            ),
            Message(
                participant=sarah,
                content='That looks amazing Mike! Where was that?',
                message_type='text',
                delay=9000
            ),
            Message(
                participant=john,
                content='Yeah, great video! I wish I could go there too.',
                message_type='text',
                delay=12000
            ),
            Message(
                participant=emma,
                content='Hey guys, sorry I\'m late to the conversation!',
                message_type='text',
                delay=15000
            ),
            Message(
                participant=emma,
                content='I also have a video to share from my weekend:',
                message_type='text',
                delay=17000
            ),
            Message(
                participant=emma,
                content='/static/chat_app/videos/sample2.mp4',
                message_type='video',
                delay=18000
            ),
            Message(
                participant=mike,
                content='That\'s awesome Emma! Looks like you had fun!',
                message_type='text',
                delay=21000
            ),
        ]
        
        Message.objects.bulk_create(messages)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with initial data!')) 