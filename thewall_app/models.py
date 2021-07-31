from login_app.models import User
from django.db import models
from django.db.models.base import Model


# Create your models here.

class Message(models.Model):
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,related_name="user_messages",on_delete=models.CASCADE)

class Comment(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    message=models.ForeignKey(Message,related_name="message_comments",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="user_comments",on_delete=models.CASCADE)

