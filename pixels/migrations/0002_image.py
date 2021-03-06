# Generated by Django 3.2.3 on 2021-05-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='post/')),
                ('image_name', models.CharField(max_length=100)),
                ('likes', models.IntegerField()),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
    ]
