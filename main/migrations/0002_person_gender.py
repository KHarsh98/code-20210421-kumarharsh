# Generated by Django 3.2 on 2021-04-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
    ]