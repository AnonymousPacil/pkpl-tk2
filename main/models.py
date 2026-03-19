from django.db import models

class Biodata(models.Model):
    nama = models.CharField(max_length=255)
    NPM = models.IntegerField()
    jenis_kelamin = models.CharField(max_length=255)
