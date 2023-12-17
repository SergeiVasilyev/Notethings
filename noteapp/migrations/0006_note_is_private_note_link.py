# Generated by Django 5.0 on 2023-12-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0005_remove_note_coeditors_note_collaborators'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='note',
            name='link',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]