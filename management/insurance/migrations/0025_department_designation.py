# Generated by Django 3.2.7 on 2021-09-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0024_auto_20210927_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
