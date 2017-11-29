from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Panel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TaskChannel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TaskOwner(models.Model):
    task_owner = models.CharField(max_length=100)


    def __str__(self):
        return self.task_owner


class Task(models.Model):
    panel = models.ForeignKey(Panel)
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    task_date = models.DateTimeField()
    task_owner = models.ForeignKey(TaskOwner)
    task_channel = models.ForeignKey(TaskChannel)
    task_text = models.TextField()
    tags = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.task_text


class TaskNote(models.Model):
    task = models.ForeignKey(Task)
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    note_text = models.TextField()

    def __str__(self):
        return self.note_text


