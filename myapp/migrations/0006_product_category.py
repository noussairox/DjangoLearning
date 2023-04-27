# Generated by Django 4.2 on 2023-04-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_test_created_test_time_alter_test_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("laptop", "laptop"),
                    ("computer", "computer"),
                    ("phone", "phone"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
