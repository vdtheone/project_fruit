# Generated by Django 4.2.2 on 2023-06-27 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0011_address_created_at_inventory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wished_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.product', unique=True),
        ),
    ]
