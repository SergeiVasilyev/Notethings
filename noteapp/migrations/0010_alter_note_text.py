# Generated by Django 5.0 on 2024-01-09 08:36

import django_editorjs_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0009_alter_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
    ]