from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.TextField()
    link = models.URLField()
    snippet = models.TextField()
    image = models.TextField(null=True)
    level = models.TextField()
    totalResults = models.FloatField()
    count = models.FloatField()
    startIndex=models.FloatField()

    def __str__(self):
        return self.title