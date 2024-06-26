# Generated by Django 5.0.4 on 2024-04-25 19:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=512)),
                ("address_line_1", models.CharField(max_length=256)),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("city_or_province", models.CharField(max_length=128)),
                ("country", models.CharField(max_length=2)),
                ("zipcode", models.CharField(max_length=16)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                "verbose_name": "address",
                "verbose_name_plural": "addresses",
                "db_table": "addresses",
            },
        ),
    ]
