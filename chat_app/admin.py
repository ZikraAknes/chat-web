from django.contrib import admin
from .models import Participant, Message

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar')
    search_fields = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('participant', 'content', 'message_type', 'timestamp', 'delay')
    list_filter = ('message_type', 'participant')
    search_fields = ('content',)
