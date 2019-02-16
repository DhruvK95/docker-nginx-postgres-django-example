from django.db import models

class ul(models.Model):
    myFile = models.FileField(upload_to='media/')