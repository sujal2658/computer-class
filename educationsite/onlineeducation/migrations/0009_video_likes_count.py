# Generated by Django 5.0.1 on 2024-03-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineeducation', '0008_video_title_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
