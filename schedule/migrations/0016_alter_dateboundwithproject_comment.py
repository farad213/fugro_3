# Generated by Django 4.1.3 on 2022-12-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0015_dateboundwithproject_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateboundwithproject',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
