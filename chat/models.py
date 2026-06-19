from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Chat(models.Model):
    chat_name = models.CharField(max_length=20 , blank = True, null= True)
    is_group = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField(max_length=200 , blank=False )
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
class Profile(models.Model):
    bio = models.TextField(max_length=250 )
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)