# Generated by Django 4.0.3 on 2022-03-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]