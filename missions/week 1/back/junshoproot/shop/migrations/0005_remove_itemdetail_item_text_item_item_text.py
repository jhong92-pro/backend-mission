# Generated by Django 4.0.1 on 2022-01-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_photo_item_alter_photo_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdetail',
            name='item_text',
        ),
        migrations.AddField(
            model_name='item',
            name='item_text',
            field=models.CharField(max_length=400, null=True),
        ),
    ]