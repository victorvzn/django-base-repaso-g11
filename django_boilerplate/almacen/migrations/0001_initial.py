# Generated by Django 4.1.7 on 2023-03-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('url_image', models.TextField()),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]