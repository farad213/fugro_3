# Generated by Django 4.1.3 on 2023-01-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JelkkodCCS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notation', models.CharField(max_length=5)),
                ('length', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='JelkodVVS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notation', models.CharField(max_length=5)),
                ('length', models.FloatField()),
            ],
        ),
    ]
