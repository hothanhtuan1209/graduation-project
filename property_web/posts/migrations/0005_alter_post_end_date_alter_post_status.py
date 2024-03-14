# Generated by Django 4.2.8 on 2024-03-14 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_alter_post_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 13, 15, 54, 29, 723767)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[
                    ("UNAPPROVED", "UNAPPROVED"),
                    ("AVAILABLE", "AVAILABLE"),
                    ("OCCUPIED", "OCCUPIED"),
                ],
                default="UNAPPROVED",
                max_length=20,
            ),
        ),
    ]
