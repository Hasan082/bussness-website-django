from django.db import models

class aboutus(models.Model):
    about_pic       = models.ImageField(upload_to='about/', blank=True, null=True)
    about_title     = models.CharField(max_length=200)
    about_desc_1    = models.TextField(blank=True, null=True)
    about_desc_2    = models.TextField(blank=True, null=True)