# Generated by Django 4.1.3 on 2022-12-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_remove_dateboundwithproject_employee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateboundwithproject',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
