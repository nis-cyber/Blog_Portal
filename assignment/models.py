from django.db import models

# Create your models here.

class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_descriptions=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural='About'


    def __str__(self):
        return self.about_heading    









class socail_platforms(models.Model):
    platforms=models.CharField(max_length=25)
    link=models.URLField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.platforms

