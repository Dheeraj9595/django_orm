# Generated by Django 5.0.3 on 2024-03-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_item_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.CharField(max_length=255),
        ),
    ]
