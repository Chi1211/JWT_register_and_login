from django.db import models

# Create your models here.
class UnitModel(models.Model):
    unit_name=models.CharField(max_length=255)
    def __str__(self):
        return self.unit_name

class MaterialModel(models.Model):
    material_name=models.CharField(max_length=255)
    material_amount=models.IntegerField()
    # unit_id=models.ForeignKey(to=UnitModel, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.material_name

