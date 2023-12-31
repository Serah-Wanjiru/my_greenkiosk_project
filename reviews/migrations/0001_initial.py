# Generated by Django 4.2.3 on 2023-07-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('message', models.TextField()),
                ('product', models.TextField()),
                ('number_of_stars', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
