# Generated by Django 3.2.6 on 2022-08-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_auto_20220805_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='guid',
            field=models.CharField(max_length=255),
        ),
    ]
