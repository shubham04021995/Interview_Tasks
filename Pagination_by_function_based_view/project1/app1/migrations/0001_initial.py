# Generated by Django 4.0.5 on 2022-06-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=50)),
            ],
        ),
    ]
