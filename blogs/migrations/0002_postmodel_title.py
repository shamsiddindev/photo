# Generated by Django 4.1 on 2022-08-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default=None, max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
    ]
