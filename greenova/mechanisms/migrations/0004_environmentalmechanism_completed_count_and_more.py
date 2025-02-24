# Generated by Django 5.1.6 on 2025-02-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mechanisms", "0003_environmentalmechanism_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="environmentalmechanism",
            name="completed_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="environmentalmechanism",
            name="in_progress_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="environmentalmechanism",
            name="not_started_count",
            field=models.IntegerField(default=0),
        ),
    ]
