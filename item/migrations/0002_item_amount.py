# Generated by Django 5.1.7 on 2025-04-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
