# Generated by Django 5.0.1 on 2024-03-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineeducation', '0002_alter_feedbackmodel_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='message',
            field=models.TextField(),
        ),
    ]