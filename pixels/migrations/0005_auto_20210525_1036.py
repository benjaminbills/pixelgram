# Generated by Django 3.2.3 on 2021-05-25 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pixels', '0004_rename_username_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comment',
        ),
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.CharField(default='Default', max_length=255),
        ),
        migrations.AddField(
            model_name='image',
            name='image_caption',
            field=models.CharField(default='Default', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='profile_photos/default_nlfwhd', upload_to='profile_photos/'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=2200)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_for', to='pixels.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
