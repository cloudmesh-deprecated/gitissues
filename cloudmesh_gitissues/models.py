from django.db import models

class Issue(models.Model):
    title = models.CharField()
    body = models.CharField()
    priority = models.CharField()
    number = models.CharField()
    assignee = models.CharField()
    labels = models.CharField()
