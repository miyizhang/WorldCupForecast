# Generated by Django 5.0.3 on 2024-03-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prediction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="matchinfo",
            name="match_time",
            field=models.CharField(max_length=8),
        ),
    ]
