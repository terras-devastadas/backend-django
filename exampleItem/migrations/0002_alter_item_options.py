# Generated by Django 5.1.3 on 2024-11-24 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exampleItem", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["name"]},
        ),
    ]
