# Generated by Django 5.0.6 on 2024-05-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/default-user-avatar.jpg', null=True, upload_to='avatars/'),
        ),
    ]
