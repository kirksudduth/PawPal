from django.db import models
from .pawpal import PawPal

class ActivityType(models.Model):
    title = models.CharField(max_length=25)
    pawPal = models.ForeignKey(PawPal, null=True, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title