# Generated by Django 4.1 on 2023-06-20 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.IntegerField(blank=True, default=0, null=True)),
                ("complete", models.BooleanField(default=False, null=True)),
                ("order_id", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("image", models.ImageField(upload_to="images")),
                ("name", models.CharField(max_length=200)),
                ("size", models.CharField(max_length=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("condition", models.CharField(max_length=10)),
                ("location", models.CharField(max_length=200)),
                ("owner", models.CharField(max_length=20)),
                ("phone_number", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.IntegerField(blank=True, default=True, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="thriftapp.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="thriftapp.product",
                    ),
                ),
            ],
        ),
    ]