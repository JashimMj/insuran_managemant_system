# Generated by Django 3.2.5 on 2021-07-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchinformation',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
