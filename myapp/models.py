from django.db import models

# Create your models here.

class Products(models.Model):
    title=models.CharField(max_length=50,verbose_name="Başlık",blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='image',blank=True,null=True)

    def __str__(self):
        return self.title