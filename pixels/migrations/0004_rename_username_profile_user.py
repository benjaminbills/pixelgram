# Generated by Django 3.2.3 on 2021-05-25 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixels', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]