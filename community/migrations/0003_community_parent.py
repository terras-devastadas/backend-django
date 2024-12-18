# Generated by Django 5.1.3 on 2024-12-14 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_community_banner_alter_community_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcommunities', to='community.community'),
        ),
    ]