from django.db import models
from ..models import *

class ParentPawPal(models.Model):
    pawpal = models.ForeignKey(PawPal, null=True, on_delete=models.CASCADE, default=None)
    parent = models.ForeignKey(Parent, null=True, on_delete=models.CASCADE, default=None)

    # def __str__(self):
    #     return f'{self.parent.user.username} is a parent of {self.pawpal.name}.'