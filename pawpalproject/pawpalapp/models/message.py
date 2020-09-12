from django.db import models
from .parent import Parent
from .pawpal import PawPal

class Message(models.Model):
    parent = models.ForeignKey(Parent, null=True, on_delete=models.CASCADE, default=None)
    pawPal = models.ForeignKey(PawPal, null=True, on_delete=models.CASCADE, default=None)
    body = models.CharField(max_length=300)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.parent.username} wrote a note on {self.when}'