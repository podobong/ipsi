# Generated by Django 3.0.5 on 2020-06-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='url',
            field=models.URLField(max_length=50),
        ),
    ]