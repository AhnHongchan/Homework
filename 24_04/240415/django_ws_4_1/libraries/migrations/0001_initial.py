# Generated by Django 4.2.11 on 2024-04-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.TextField()),
                ('pubdate', models.DateField()),
                ('price', models.IntegerField()),
                ('adult', models.BooleanField()),
            ],
        ),
    ]
