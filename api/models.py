from django.db import models

# Create your models here.
class Task(models.Model):
    # title is to store Strings
    # completed is used to store True/False
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False,blank=True,null=True)
    objects=models.Manager()

    def __str__(self):
        return self.title