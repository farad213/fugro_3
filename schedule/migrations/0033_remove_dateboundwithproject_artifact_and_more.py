# Generated by Django 4.1.3 on 2022-12-18 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0032_remove_dateboundwithproject_artifact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dateboundwithproject',
            name='artifact',
        ),
        migrations.RemoveField(
            model_name='dateboundwithproject',
            name='subproject',
        ),
        migrations.AddField(
            model_name='dateboundwithproject',
            name='artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.artifact'),
        ),
        migrations.AddField(
            model_name='dateboundwithproject',
            name='subproject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.subproject'),
        ),
    ]
