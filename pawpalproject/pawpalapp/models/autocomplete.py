from django.db import models

class AutoComplete(models.Model):
    pawpalname = models.CharField(max_length=50)
    class Meta:
        db_table="pawpals"