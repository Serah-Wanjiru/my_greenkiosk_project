# Generated by Django 4.2.3 on 2023-07-11 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_management',
            name='order',
        ),
        migrations.RemoveField(
            model_name='payment_management',
            name='status',
        ),
    ]
