from django.db import models

class student (models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=35)
    course=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.stuid},{self.stuname},{self.course}'
