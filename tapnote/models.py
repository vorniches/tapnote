import uuid
from django.db import models
from django.utils import timezone

class Note(models.Model):
    hashcode = models.CharField(max_length=32, unique=True)
    content = models.TextField()
    edit_token = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note {self.hashcode}"

    def save(self, *args, **kwargs):
        if not self.hashcode:
            self.hashcode = uuid.uuid4().hex
        if not self.edit_token:
            self.edit_token = uuid.uuid4().hex
        super().save(*args, **kwargs) 