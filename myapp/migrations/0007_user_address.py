# Generated by Django 5.2 on 2025-04-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Ahmedabad', max_length=100),
        ),
    ]
