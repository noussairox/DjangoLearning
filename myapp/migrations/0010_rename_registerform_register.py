# Generated by Django 4.2 on 2023-04-27 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_registerform_alter_lg_name"),
    ]

    operations = [
        migrations.RenameModel(old_name="RegisterForm", new_name="Register",),
    ]
