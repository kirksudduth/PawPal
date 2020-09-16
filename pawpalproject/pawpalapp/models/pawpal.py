from django.db import models


class PawPal(models.Model):
    
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    favorite_treat = models.CharField(max_length=30)
    favorite_toy = models.CharField(max_length=30)
    image = models.ImageField(default='jowls.png', upload_to='..images')

    def __str__(self):
        return self.name