# Generated by Django 4.1.6 on 2023-03-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ghjgjjgj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
