from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
