# Generated by Django 4.1.2 on 2022-12-19 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import thoughtsapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thoughtsapp', '0003_rename_title_catagory_new_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to=thoughtsapp.models.getfilename)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]