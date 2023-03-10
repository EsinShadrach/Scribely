# Generated by Django 4.1.2 on 2023-01-24 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_note_id_note_unique_note_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='unique_note_identity',
            field=models.UUIDField(default=uuid.UUID('cfc3ba4f-682f-4ace-9364-665eb4f32ac8'), primary_key=True, serialize=False),
        ),
    ]
