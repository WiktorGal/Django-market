# Generated by Django 4.2.1 on 2023-07-05 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='careated_at',
            new_name='created_at',
        ),
    ]
