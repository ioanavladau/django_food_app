from django.db import models

# Create your models here.
class RecipeData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200, default='lunch')
    image = models.ImageField(upload_to='recipe-images/', default="recipe-images/none/noimg.jpg")