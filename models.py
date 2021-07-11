from django.db import models
class mode(models.Model):





    #name=models.CharField(max_length=10)
    #name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='')
    def __str__(self):
        return str(self.image)


# Create your models here.
