# Generated by Django 4.2.13 on 2024-05-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='asdf', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
