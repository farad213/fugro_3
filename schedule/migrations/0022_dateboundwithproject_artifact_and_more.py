# Generated by Django 4.1.3 on 2022-12-10 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_dateboundwithproject_subproject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateboundwithproject',
            name='artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.artifact'),
        ),
        migrations.AddField(
            model_name='dateboundwithproject',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.profile'),
        ),
    ]