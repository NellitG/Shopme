# Generated by Django 5.2.4 on 2025-07-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=255, unique=True)),
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
