from django.db import models

# Create your models here.
#makemigrations  - create changes and store in a file
# migrate - apply the pending changes create by makemigrations


class Job(models.Model):
    jobrole=models.CharField(max_length=122)
    quali=models.CharField(max_length=122)
    speci=models.CharField(max_length=122)
    loca=models.TextField()
    sal=models.IntegerField()
    date=models.DateField()

    