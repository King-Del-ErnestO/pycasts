from django.db import models

# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    pub_date = models.DateTimeField()
    link = models.URLField(max_length=255)
    image = models.URLField(max_length=255)
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"