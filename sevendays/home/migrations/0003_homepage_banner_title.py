# Generated by Django 5.0.9 on 2024-10-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Welcome to my homepage!', max_length=100),
        ),
    ]
