# Generated by Django 4.0.4 on 2022-06-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner_alter_entry_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
