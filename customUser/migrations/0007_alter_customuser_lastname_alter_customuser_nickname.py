# Generated by Django 5.1.3 on 2024-12-28 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0006_rename_name_customuser_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='lastName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nickName',
            field=models.CharField(max_length=30),
        ),
    ]
