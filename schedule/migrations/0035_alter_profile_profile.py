# Generated by Django 4.1.3 on 2022-12-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0034_profile_length_profile_measurement_side_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.CharField(max_length=50, null=True, verbose_name='Szelvény'),
        ),
    ]
