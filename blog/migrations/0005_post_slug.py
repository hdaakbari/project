# Generated by Django 4.2.6 on 2023-10-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_dislike_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
