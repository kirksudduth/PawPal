from django.db import models
from ..models import *

class Activity(models.Model):

    pawpal = models.ForeignKey(PawPal, null=True, on_delete=models.CASCADE, default=None)
    parent = models.ForeignKey(Parent, null=True, on_delete=models.CASCADE, default=None)
    activity_type = models.ForeignKey(ActivityType, null=True, on_delete=models.CASCADE, default=None)
    note = models.CharField(max_length=140)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pawpal.name} did {self.activity_type.title} on {self.when}.'