# Generated by Django 4.2.4 on 2025-05-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DailyPrice",
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
                ("code", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("close", models.IntegerField()),
                ("open", models.IntegerField()),
                ("high", models.IntegerField()),
                ("low", models.IntegerField()),
                ("volume", models.BigIntegerField()),
            ],
            options={
                "unique_together": {("code", "date")},
            },
        ),
    ]
