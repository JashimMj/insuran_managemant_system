# Generated by Django 3.2.5 on 2021-07-15 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0007_userprofilem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilem',
            name='Email',
        ),
    ]
