from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name