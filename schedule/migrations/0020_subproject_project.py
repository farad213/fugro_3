# Generated by Django 4.1.3 on 2022-12-10 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0019_artifact_artifact'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproject',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.project'),
        ),
    ]
