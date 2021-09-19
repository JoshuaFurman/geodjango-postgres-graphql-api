from django.contrib.gis.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    coordinates = models.PointField()

    def __str__(self):
        return self.title
