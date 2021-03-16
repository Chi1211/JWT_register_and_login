from django.db import models

# Create your models here.


class MaterialModel(models.Model):
    material_name=models.CharField(max_length=255)

    def __str__(self):
        return self.material_name

    