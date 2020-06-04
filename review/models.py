from django.db import models


class Review(models.Model):
    university = models.CharField(unique=True, max_length=20)
    url = models.CharField(max_length=50)

    def __str__(self):
        return str(self.university)