from django.conf import settings
from django.db import models
from django.utils import timezone


class Role(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    due_date =  models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    role_id = models.ForeignKey(Role, on_delete = models.CASCADE)

    def publish(self):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title