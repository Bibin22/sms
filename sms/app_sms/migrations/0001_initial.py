# Generated by Django 3.2 on 2021-04-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('item', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
