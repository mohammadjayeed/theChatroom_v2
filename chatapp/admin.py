from django.contrib import admin
from .models import ChatRoom, ChatMessage


# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(ChatMessage)