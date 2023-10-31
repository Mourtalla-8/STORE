# Generated by Django 4.2.6 on 2023-10-31 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='order_date',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
