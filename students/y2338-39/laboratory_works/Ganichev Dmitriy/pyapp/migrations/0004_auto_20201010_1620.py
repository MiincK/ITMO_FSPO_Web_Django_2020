# Generated by Django 3.0.10 on 2020-10-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyapp', '0003_furgathering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furdelivery',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='furgathering',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='furshipment',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
