# Generated by Django 4.1.3 on 2022-12-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0025_alter_dateboundwithproject_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Szelvény'),
        ),
    ]