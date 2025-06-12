from django.db import models

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255, default='/static/chat_app/images/avatar.png')
    
    def __str__(self):
        return self.name

class Message(models.Model):
    MESSAGE_TYPES = (
        ('text', 'Text'),
        ('video', 'Video'),
        ('image', 'Image'),
    )
    
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    content = models.TextField()
    caption = models.TextField(blank=True, null=True)  # Optional caption field for image messages
    timestamp = models.DateTimeField(auto_now_add=True)
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='text')
    delay = models.IntegerField(default=3000)  # Delay in milliseconds before this message appears
    
    def __str__(self):
        return f"{self.participant.name}: {self.content[:20]}..."
