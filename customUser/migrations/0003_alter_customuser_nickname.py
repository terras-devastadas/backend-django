# Generated by Django 5.1.3 on 2024-12-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0002_alter_customuser_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nickName',
            field=models.CharField(max_length=30),
        ),
    ]
