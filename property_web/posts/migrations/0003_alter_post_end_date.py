# Generated by Django 4.2.8 on 2024-03-15 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 14, 9, 49, 45, 872345)
            ),
        ),
    ]
