from django.db import models
from ..models import *

class ParentPawPal(models.Model):
    pawpal = models.ForeignKey(PawPal, null=True, on_delete=models.CASCADE, default=None)
    parent = models.ForeignKey(Parent, null=True, on_delete=models.CASCADE, default=None)
    