# Generated by Django 2.1.5 on 2019-02-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
