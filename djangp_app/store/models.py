from django.db import models


class Categories(models.Model):
    nom = models.CharField(max_length=100, null=False , blank=False)
    def __str__(self):
        return self.nom



class ViewPhoto(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    images = models.ImageField(null= False, blank= False)
    description = models.TextField()

    def __str__(self):
        return self.description
# Create your models here.
