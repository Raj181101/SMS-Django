# Generated by Django 2.2.5 on 2019-09-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Birthday', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birth',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
