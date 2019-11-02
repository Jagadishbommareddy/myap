from django.db import models
from django.contrib import admin
# Create your models here.


class UserObj(models.Model):
    text_data = models.CharField(max_length=255)

    def __str__(self):
        return self.text_data


class SystemConfig(models.Model):
    parameter = models.CharField(max_length=255)
    value = models.IntegerField()


class PdfUpload(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    file = models.FileField(default="")


admin.site.register(UserObj)
admin.site.register(SystemConfig)
admin.site.register(PdfUpload)