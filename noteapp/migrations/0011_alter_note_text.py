# Generated by Django 5.0 on 2024-01-26 09:02

import noteapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0010_alter_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=noteapp.models.CustomQuillField(blank=True, null=True),
        ),
    ]