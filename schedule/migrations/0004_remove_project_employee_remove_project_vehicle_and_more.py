# Generated by Django 4.1.3 on 2022-12-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_remove_dates_project_dates_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(null=True, to='schedule.employee'),
        ),
        migrations.AddField(
            model_name='project',
            name='vehicle',
            field=models.ManyToManyField(null=True, to='schedule.vehicle'),
        ),
    ]
