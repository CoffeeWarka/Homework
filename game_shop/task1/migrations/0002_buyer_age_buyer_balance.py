# Generated by Django 4.2.17 on 2024-12-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
