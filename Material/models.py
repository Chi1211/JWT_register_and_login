from django.db import models

# Create your models here.
class UnitModel(models.Model):
    unit_name=models.CharField(max_length=50)

    def __str__(self):
        return self.unit_name

class MaterialModel(models.Model):
    material_name=models.CharField(max_length=255)
    material_amount=models.IntegerField()
    unit_name=models.ForeignKey(UnitModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.material_name

    