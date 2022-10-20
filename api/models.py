from django.db import models


# Create your models here.

class Resource(models.Model):
    """This model is for the Resource file which needs to be validated
    """
    name = models.CharField(primary_key=True, max_length=255)  # name of the resource file
    location = models.CharField(max_length=255)  # location of the resource file in the file system
    resource_name = models.CharField(max_length=255)  # name of the dataset to which the Resource file belongs
