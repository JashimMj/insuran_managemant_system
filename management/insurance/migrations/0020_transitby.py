# Generated by Django 3.2.5 on 2021-09-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0019_alter_bankbranch_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransitBy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]