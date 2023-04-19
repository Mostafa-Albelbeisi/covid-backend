from django.db import models

# Create your models here.


class Covid19(models.Model):
    id = models.AutoField(primary_key=True)
    countriesName = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.countriesName