# Generated by Django 4.1.3 on 2023-03-31 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_remove_vehicle_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='archived',
            field=models.DateField(null=True, verbose_name='Archiválva'),
        ),
    ]