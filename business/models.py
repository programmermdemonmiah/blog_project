from django.db import models
from django.core.exceptions import ValidationError

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    def clean(self):
        if not self.name:
            raise ValidationError({"name": "Name is required."})

        if len(self.subject) < 5:
            raise ValidationError({"subject": "Subject must be at least 5 characters."})


    def save_contact(self):
        self.full_clean()
        self.save()