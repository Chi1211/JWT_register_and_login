from django.db import models

# Create your models here.
class CategoriesModel(models.Model):
    category_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name

class FoodModel(models.Model):
    food_name=models. CharField(max_length=255)
    food_price=models.DecimalField(max_digits=19,  decimal_places=2)
    status=models.BooleanField(default=True)
    category=models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)