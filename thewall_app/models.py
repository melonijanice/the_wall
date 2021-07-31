from login_app.models import User
from django.db import models
from django.db.models.base import Model


# Create your models here.
class MessageManager(models.Manager):
    def wall_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        return errors


class Message(models.Model):
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,related_name="user_messages",on_delete=models.CASCADE)
    objects=MessageManager()

class Comment(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    message=models.ForeignKey(Message,related_name="message_comments",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="user_comments",on_delete=models.CASCADE)

