# Generated by Django 4.2.13 on 2024-08-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_product_tot_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone_Number',
            field=models.BigIntegerField(null=True),
        ),
    ]