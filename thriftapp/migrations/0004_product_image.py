# Generated by Django 4.1 on 2023-06-20 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thriftapp", "0003_remove_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(default=0, upload_to="images"),
            preserve_default=False,
        ),
    ]
