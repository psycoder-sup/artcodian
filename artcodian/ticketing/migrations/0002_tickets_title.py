# Generated by Django 2.2.1 on 2019-06-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
