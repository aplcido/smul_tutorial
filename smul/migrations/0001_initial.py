# Generated by Django 4.0 on 2021-12-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Shurt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(db_index=True, unique=True)),
                ('code', models.CharField(db_index=True, max_length=10, unique=True)),
            ],
        ),
    ]
