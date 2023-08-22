from django.db import models

class aboutus(models.Model):
    about_pic                   = models.ImageField(upload_to='about/', blank=True, null=True)
    about_title                 = models.CharField(max_length=200)
    about_readmore_btn_text     = models.CharField(max_length=100, default="Read More")
    about_readmore_btn_url      = models.CharField(max_length=255, default="#")
    about_desc_1                = models.TextField(blank=True, null=True)
    about_desc_2                = models.TextField(blank=True, null=True)

