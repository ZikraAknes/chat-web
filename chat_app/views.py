from django.shortcuts import render
from django.http import JsonResponse
from .models import Participant, Message
import json

def home(request):
    participants = Participant.objects.all()
    messages = Message.objects.all().order_by('id')
    
    # Create a participant name string for the header with limit
    participant_list = [p.name for p in participants]
    
    participant_names = ", ".join(participant_list)

    if len(participant_names) > 30:
        participant_names = participant_names[:30] + "..."
    
    return render(request, 'chat_app/index.html', {
        'participants': participants, 
        'messages': messages,
        'participant_names': participant_names
    })
