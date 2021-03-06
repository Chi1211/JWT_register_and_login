# Generated by Django 2.2 on 2021-03-16 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_table_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255)),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_table_manager.CategoriesModel')),
            ],
        ),
    ]
