# Generated by Django 3.2 on 2021-04-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.PositiveIntegerField()),
                ('bmi_cat', models.CharField(max_length=100)),
                ('health_risk', models.CharField(max_length=100)),
            ],
        ),
    ]