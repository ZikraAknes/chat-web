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

def get_messages(request):
    messages = Message.objects.all().order_by('id')
    message_list = []
    
    for message in messages:
        message_list.append({
            'id': message.id,
            'participant_id': message.participant.id,
            'participant_name': message.participant.name,
            'participant_avatar': message.participant.avatar,
            'content': message.content,
            'message_type': message.message_type,
            'delay': message.delay,
            'timestamp': message.timestamp.strftime('%I:%M %p')
        })
    
    return JsonResponse({'messages': message_list})
