from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='photos')
    descreption=models.TextField()

    def __str__(self):
        return self.name