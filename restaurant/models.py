from django.db import models

# Create your models here.
class user(models.Model):
    models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return f'{self.name}'