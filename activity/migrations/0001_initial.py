# Generated by Django 5.0.3 on 2024-04-17 20:52

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ActivityBooking",
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
                (
                    "cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                ("link", models.URLField(blank=True, max_length=1000, null=True)),
                ("start_date_time", models.DateTimeField()),
                ("end_date_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("canceled", "Canceled"),
                            ("completed", "Completed"),
                            ("confirmed", "Confirmed"),
                            ("pending", "Pending"),
                        ],
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admin_bookings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "invitees",
                    models.ManyToManyField(
                        related_name="invitee_bookings", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "activity",
                "verbose_name_plural": "activities",
                "db_table": "bookings_activity",
                "ordering": ("-created_at",),
                "get_latest_by": "created_by",
            },
        ),
        migrations.CreateModel(
            name="ActivityComment",
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
                (
                    "rating",
                    models.DecimalField(
                        choices=[
                            (0, "0"),
                            (0.5, "0.5"),
                            (1, "1"),
                            (1.5, "1.5"),
                            (2, "2"),
                            (2.5, "2.5"),
                            (3, "3"),
                            (3.5, "3.5"),
                            (4, "4"),
                            (4.5, "4.5"),
                            (5, "5"),
                        ],
                        decimal_places=1,
                        default=0,
                        help_text="Rating on a scale of 0 to 5 in increments of 0.5",
                        max_digits=2,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "activity_booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="activity.activitybooking",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
                "db_table": "comments",
                "ordering": ("-created_at",),
                "get_latest_by": "created_at",
            },
        ),
        migrations.CreateModel(
            name="HistoricalActivityBooking",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                ("link", models.URLField(blank=True, max_length=1000, null=True)),
                ("start_date_time", models.DateTimeField()),
                ("end_date_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("canceled", "Canceled"),
                            ("completed", "Completed"),
                            ("confirmed", "Confirmed"),
                            ("pending", "Pending"),
                        ],
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical activity",
                "verbose_name_plural": "historical activities",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalActivityComment",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(
                        choices=[
                            (0, "0"),
                            (0.5, "0.5"),
                            (1, "1"),
                            (1.5, "1.5"),
                            (2, "2"),
                            (2.5, "2.5"),
                            (3, "3"),
                            (3.5, "3.5"),
                            (4, "4"),
                            (4.5, "4.5"),
                            (5, "5"),
                        ],
                        decimal_places=1,
                        default=0,
                        help_text="Rating on a scale of 0 to 5 in increments of 0.5",
                        max_digits=2,
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "activity_booking",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="activity.activitybooking",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical comment",
                "verbose_name_plural": "historical comments",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
