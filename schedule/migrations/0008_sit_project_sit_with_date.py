# Generated by Django 4.1.3 on 2023-02-17 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_delete_test45'),
    ]

    operations = [
        migrations.CreateModel(
            name='SIT_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_no', models.CharField(max_length=30)),
                ('customer', models.CharField(max_length=50)),
                ('contract', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SIT_with_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bridge', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('no_of_piles', models.IntegerField()),
                ('date_bound_with_project_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.dateboundwithproject')),
                ('project_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.sit_project')),
            ],
        ),
    ]