# Generated by Django 5.1.3 on 2024-12-28 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0007_alter_customuser_lastname_alter_customuser_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='nickName',
            new_name='firstName',
        ),
    ]