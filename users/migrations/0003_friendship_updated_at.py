# Generated by Django 5.0.6 on 2024-06-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_friends_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
