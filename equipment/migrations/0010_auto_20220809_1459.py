# Generated by Django 3.0 on 2022-08-09 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0009_auto_20220809_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.Driver'),
        ),
    ]
