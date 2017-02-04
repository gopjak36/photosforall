from django.db import models
from django.utils import timezone

class Photo(models.Model):
    link = models.CharField(max_length = 400)
    title = models.CharField(max_length = 250)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
